from sys import argv, stderr
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

# Let's also look at how much attention probs agree on each output, for each model
# and how