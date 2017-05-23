from sys import argv, stderr
import codecs
from collections import Counter

def get_candidates(i, data, n):
  candidates = []
  for j in range(n):
    candidates.append(data[j][i].split("\t")[1])

  return candidates


if __name__ == '__main__':
  if len(argv) < 2:
    stderr.write("USAGE: %s prefix [N]")
    exit(1)

  N = int(argv[2])
  '''
  data_sets = []
  for i in range(1, N + 1):
    data_sets.append(open("%s.%u.sys" % (argv[1], i)).read().split('\n'))
    data_sets[-1] = [wf for wf in data_sets[-1] if wf != '']

  correct_data = open("%s" % argv[3]).read().strip().split('\n')
  correct = [x.split("\t")[1] for x in correct_data]

  correct_count = 0
  ties = 0
  unique_candidates = []
  for i in range(len(data_sets[0])):
    candidates = get_candidates(i,data_sets,N)
    candidate_counts = Counter(candidates)
    unique_candidates.append(len(set(candidates)))
    if correct[i] in candidates:
      if max(candidate_counts.values()) == candidate_counts[correct[i]] and list(candidate_counts.values()).count(candidate_counts[correct[i]]) > 1:
        ties+=1

      correct_count+=1


  print(correct_count * 100.0 / len(correct))
  print("Average number of unique candidates: %.2f" % (float(sum(unique_candidates)) / float(len(unique_candidates))))
  print("%% of examples with a a first place tie with correct candidate: %.2f%%" % (ties * 100 / len(correct)))
'''
  # Let's also look at how much attention probs agree on each output, for each model
  import os
  # 1000 x 10 list of (cand, prob) tuples
  model_prob_data = []
  for fn in os.listdir('model_probs/encdec_models'):
    with codecs.open('model_probs/encdec_models/%s' % fn, 'r', "utf-8") as data:
      lines = [line.strip() for line in data]
      for i, cand_prob in enumerate(lines):
        model_prob_data.append([])
        cand_prob_tup= tuple(cand_prob.split("\t"))
        model_prob_data[i].append(cand_prob_tup)


  with codecs.open("all/task1/spanish-dev", 'r', "utf-8") as devdata:
    devlines = [line.strip() for line in devdata]

  candidate_distr = {}
  for lex in model_prob_data:
    for i, candidate_prob in enumerate(lex):
      try:
        cand, prob = candidate_prob
      except:
        print(i)
        print(lex)
        print(candidate_prob)
      candidate_distr.setdefault(cand, []).append(prob)

#    for cand, distr in candidate_distr.items():
#      print("%s: %f" % (cand, sum(float(x) for x in distr)))

    # So maybe check variance, prob aggreement on correct, prob agreement on incorrect, etc?
  # and how much the total dev accuracies vary per model
