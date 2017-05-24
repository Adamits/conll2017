encdec_results/dutch-test.medium.sys:

	python3 scripts/vote.py encdec_results/dutch-test.medium 9 > encdec_results/dutch-test.medium.sys
	python3 scripts/vote_odds.py encdec_results/dutch-test.medium all/task1/dutch-dev 9 > encdec_results/dutch-test.medium.sys.vote-odds
	python3 scripts/vote_gib_sampling.py encdec_results/dutch-test.medium all/task1/dutch-dev 9 > encdec_results/dutch-test.medium.sys.vote-gibb
	python3 scripts/vote_odds_top_3.py encdec_results/dutch-test.medium all/task1/dutch-dev 9 > encdec_results/dutch-test.medium.sys.vote-odds-top-3

	python2.7 ./evaluation/evalm.py --guess encdec_results/dutch-test.medium.sys --gold encdec_results/dutch-500-dev --task 1
	python2.7 ./evaluation/evalm.py --guess encdec_results/dutch-test.medium.sys.vote-odds --gold encdec_results/dutch-500-dev --task 1
	python2.7 ./evaluation/evalm.py --guess encdec_results/dutch-test.medium.sys.vote-gibb --gold encdec_results/dutch-500-dev --task 1
	python2.7 ./evaluation/evalm.py --guess encdec_results/dutch-test.medium.sys.vote-odds-top-3 --gold encdec_results/dutch-500-dev --task 1