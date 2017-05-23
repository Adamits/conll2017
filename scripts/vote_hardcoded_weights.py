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

def adjust_weights(alpha, weights):
    # randomly move weight alpha form one classifier to another
    from_i, to_i = random.sample(range(0, 9), 2)
    weights[from_i] -= alpha
    weights[to_i] += alpha
    return weights

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
    gold_data = [line.strip().split("\t") for line in dev_lines]
    # For storing optimal weights through all iterations
    # pi / 1 - pi AKA dev_acc / (1 - dev_acc)
    weights = {0: 0.11200000000000002, 1: 0.12400000000000001, 2: 0.088000000000000023, 3: 0.14800000000000002, 4: -0.27200000000000008, 5: 0.36400000000000021, 6: 0.24400000000000011, 7: -0.055999999999999946, 8: -0.091999999999999957, 9: 0.34000000000000019}
    acc = 0
    guesses = []
    # for each model get
    for j in range(len(data_sets[0])):
        guesses.append(vote(j,data_sets,N, weights).split("\t"))
    # Update accuracy per weights
    acc = eval(gold_data, guesses)
    print(acc)

    for i in range(len(data_sets[0])):
        print(vote(i, data_sets, N, weights))