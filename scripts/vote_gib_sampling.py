from sys import argv, stderr
from collections import defaultdict as dd
import random
import codecs
import numpy as np
from copy import copy

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

def adjust_weights(alpha, weights, n):
    # randomly move weight alpha form one classifier to another
    new_weights = copy(weights)
    from_i, to_i = random.sample(range(0, n), 2)
    new_weights[from_i] -= alpha
    new_weights[to_i] += alpha

    # Make sure the adjustment doesn't make a weight go negative
    # If it does, recursively call function again
    if sum(1 for w in new_weights.values() if w < 0.0) > 0:
        return adjust_weights(alpha, weights, n)
    else:
        return new_weights

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
    tuning_data = dev_data[:499]
    gold_data = dev_data[499:]
    # For storing optimal weights through all iterations
    optimal_acc = 0
    # Just hardcode alphas for now
    alphas = np.arange(0.01, 0.06, 0.01)
    same = 0
    # Test with each alpha value
    for alpha in alphas:
        weights = dd(lambda: 1 / N)
        acc = 0
        for i in range(2000):
            last_acc = acc

            # Get guesses with current weights
            guesses = []
            for j in range(len(tuning_data)):
                guesses.append(vote(j,data_sets,N, weights).split("\t"))
            # Update accuracy per weights
            acc = eval(tuning_data, guesses)

            if acc == last_acc:
                same += 1

            # Store global optima
            if acc > optimal_acc:
                optimal_weights = copy(weights)
                optimal_acc = acc
                optimal_alpha = alpha

            # Use new weight distribution if it is better, or only slightly worse
            if acc > last_acc:
                # Get a new set of weights given the previous weights
                last_weights = weights
                weights = adjust_weights(alpha, weights, N)
            elif random.uniform(0, 1.0) < (acc / last_acc):
                last_weights = weights
                weights = adjust_weights(alpha, weights, N)
            # Otherwise try adjusting the previous set of weights
            else:
                weights = adjust_weights(alpha, last_weights, N)

    for k in range(499, 1000):
        print(vote(k, data_sets, N, optimal_weights))

    print(same)
