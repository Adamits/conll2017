from sys import argv, stderr
from collections import defaultdict as dd
import random
import codecs
import numpy as np

def eval(golds, guesses):
    corr_count = 0
    for i in range(len(golds) - 1):
        _, corr, _ = golds[i]
        _, guess, _ = guesses[i]
        if corr == guess:
            corr_count += 1

    return round(corr_count / len(golds) * 100, 2)


def vote(i,data,n, weights):
    counts = dd(float)
    for j in range(n):
        counts[data[j][i]] += weights[j]
    return sorted([(v,k) for k,v in counts.items()],reverse=1)[0][1]

if __name__=='__main__':
    if len(argv) < 3:
        stderr.write("USAGE: %s prefix [N]")
        exit(1)

    N = 10
    if len(argv) == 4:
        N = int(argv[3])

    data_sets = []
    for i in range(1,N+1):
        data_sets.append(open("%s.%u.sys" % (argv[1],i)).read().split('\n'))
        data_sets[-1] = [wf for wf in data_sets[-1] if wf != '']

    # Get gold data for eval
    dev_lines = codecs.open(argv[2], 'r', 'utf-8')
    dev_data = [line.strip().split("\t") for line in dev_lines]

    tuning_data = dev_data[:900]
    gold_data = dev_data[900:]
    # For storing optimal weights through all iterations
    # pi / 1 - pi AKA dev_acc / (1 - dev_acc)
    weights = dd(lambda: 1 / N)
    acc = 0
    dev_acc = 0.0
    # for each model get
    for i in range(N):
        # Update accuracy per weights
        dev_acc = eval(tuning_data, [l.split("\t") for l in data_sets[i][:len(tuning_data)]]) / 100
        weights[i] = dev_acc / (1 - dev_acc)

    for k in range(900, 1000):
        print(vote(k, data_sets, N, weights))