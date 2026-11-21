#!/usr/bin/env python3
"""Read-only audit of the frozen 13-window SHAP/LIME stability export.

Input files are NOT part of the initial release ZIP. This script accepts the
consolidated CSVs exported from the original completed Checkpoint 6A.
"""
import argparse
import csv
import math
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from statistics import mean, stdev

SEEDS = {42, 123, 456, 789, 2026}
EXPECTED = {
    ("SHAP", "UK-DALE"): (5, 1.000000, 0.000000),
    ("SHAP", "AMPds2"): (8, 0.9666666666666667, 0.0617213399848368),
    ("LIME", "UK-DALE"): (5, 0.7923809523809524, 0.143514),
    ("LIME", "AMPds2"): (8, 0.85, 0.0308606699924184),
}
FILES = {
    'runs': 'all_130_explanation_runs.csv',
    'features': 'all_2990_original_feature_records.csv',
    'pairs': 'all_260_pairwise_jaccard.csv',
    'windows': 'window_level_26_method_records.csv',
    'groups': 'dataset_and_overall_summaries.csv',
}

def rows(path):
    with path.open('r', newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def checked(condition, message):
    if not condition:
        raise AssertionError(message)

def truthy(value):
    return value.lower() == 'true'

def approx(a, b, tol=1e-9):
    return math.isclose(float(a), float(b), abs_tol=tol, rel_tol=0)

def audit(root):
    contents = {k:rows(root/v) for k,v in FILES.items()}
    checked([len(contents[k]) for k in FILES] == [130,2990,260,26,6], 'Record-count mismatch')
    run_keys = set()
    run_by_group = defaultdict(list)
    feature_by_run = defaultdict(list)
    pair_by_group = defaultdict(list)
    window_by_group = {}
    for r in contents['runs']:
        key=(r['method'],r['window_id'],int(r['seed']))
        checked(key not in run_keys, f'Duplicate run {key}')
        run_keys.add(key)
        run_by_group[key[:2]].append(r)
    for f in contents['features']:
        feature_by_run[(f['method'],f['window_id'],int(f['seed']))].append(f)
    for p in contents['pairs']:
        pair_by_group[(p['method'],p['window_id'])].append(p)
    for w in contents['windows']:
        key=(w['method'],w['window_id'])
        checked(key not in window_by_group,f'Duplicate summary {key}')
        window_by_group[key]=w
    checked(len(run_by_group)==26 and set(run_by_group)==set(window_by_group),'Window-method mismatch')
    series=defaultdict(list)
    j_total=0
    max_additive=0.0
    for group, runs in run_by_group.items():
        method,window=group
        dataset='UK-DALE' if window.startswith('UKDALE_') else 'AMPds2'
        checked(len(runs)==5 and {int(r['seed']) for r in runs}==SEEDS,f'Incomplete runs {group}')
        for run in runs:
            seed=int(run['seed'])
            features=feature_by_run[(method,window,seed)]
            checked(len(features)==23 and len({int(x['feature_index']) for x in features})==23,f'Feature rows {group}:{seed}')
            top={int(f['feature_index']) for f in features if truthy(f['top5'])}
            checked(len(top)==5, f'Invalid top-five count {group}:{seed}')
            values={int(f['feature_index']):float(f['shap_value'] if method=='SHAP' else f['lime_weight'])
                    for f in features if (method=='SHAP' or truthy(f['selected_in_surrogate']))}
            if method=='SHAP':
                checked(len(values)==23,f'SHAP values missing {group}:{seed}')
                add=abs(float(run['expected_value'])+sum(values.values())-float(run['anomaly_score']))
                max_additive=max(max_additive,add)
                checked(add<1e-9,f'Additivity mismatch {group}:{seed}')
            else:
                checked(len(values)==10,f'LIME selected features != 10 {group}:{seed}')
                checked(math.isfinite(float(run['local_r2'])),f'LIME R2 invalid {group}:{seed}')
            calculated_top={i for i,_ in sorted(values.items(),key=lambda z:(-abs(z[1]),z[0]))[:5]}
            checked(top==calculated_top,f'Top-five identity mismatch {group}:{seed}')
        jaccards=[]
        pairs=pair_by_group[group]
        checked(len(pairs)==10,f'Pair count mismatch {group}')
        checked({tuple(sorted((int(p['seed_a']),int(p['seed_b'])))) for p in pairs}==set(combinations(sorted(SEEDS),2)),f'Pair set mismatch {group}')
        for p in pairs:
            a={int(f['feature_index']) for f in feature_by_run[method,window,int(p['seed_a'])] if truthy(f['top5'])}
            b={int(f['feature_index']) for f in feature_by_run[method,window,int(p['seed_b'])] if truthy(f['top5'])}
            jac=len(a&b)/len(a|b)
            checked(approx(jac,p['top5_jaccard']),f'Pairwise Jaccard mismatch {group}')
            jaccards.append(jac)
            j_total+=1
        wm=mean(jaccards)
        checked(approx(wm,window_by_group[group]['mean_top5_jaccard']),f'Window-level mean mismatch {group}')
        series[method,dataset].append(wm)
    checked(j_total==260, 'Total pair count mismatch')
    print('PASS: 130 runs, 2990 original-feature records and 260 pairwise Jaccards')
    print(f'PASS: Maximum SHAP reconstruction additivity error: {max_additive:.3e}')
    for method,dataset in [('SHAP','UK-DALE'),('SHAP','AMPds2'),('LIME','UK-DALE'),('LIME','AMPds2')]:
        arr=series[method,dataset]
        n,expected_mean,expected_sd=EXPECTED[method,dataset]
        checked(len(arr)==n,f'Window count mismatch {method}/{dataset}')
        checked(approx(mean(arr),expected_mean,2e-5) and approx(stdev(arr),expected_sd,2e-5),f'Published result mismatch {method}/{dataset}')
        print(f'PASS {method:4s} {dataset:7s}: windows={n}, Jaccard={mean(arr):.4f} ± {stdev(arr):.4f}')
    overall={method:series[method,'UK-DALE']+series[method,'AMPds2'] for method in ('SHAP','LIME')}
    for method,expected in (('SHAP',0.9794871794871794),('LIME',0.8278388278388278)):
        checked(approx(mean(overall[method]),expected,1e-9),f'Overall result mismatch for {method}')
    print('PASS: 26 window-method summaries; overall published values reconciled')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence-dir',type=Path,required=True)
    audit(parser.parse_args().evidence_dir)
