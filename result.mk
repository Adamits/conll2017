encdec_results/finnish-test.low.sys:

	python3 scripts/vote.py encdec_results/finnish-test.low > encdec_results/finnish-test.low.sys
	python3 scripts/vote_weights_basic.py encdec_results/finnish-test.low all/task1/finnish-dev > encdec_results/finnish-test.low.sys.weighted-votes-basic
	python3 scripts/vote_weights.py encdec_results/finnish-test.low all/task1/finnish-dev > encdec_results/finnish-test.low.sys.weighted-votes

	python2.7 ./evaluation/evalm.py --guess encdec_results/finnish-test.low.sys --gold encdec_results/finnish-100-dev --task 1
	python2.7 ./evaluation/evalm.py --guess encdec_results/finnish-test.low.sys.weighted-votes-basic --gold encdec_results/finnish-100-dev --task 1
	python2.7 ./evaluation/evalm.py --guess encdec_results/finnish-test.low.sys.weighted-votes --gold encdec_results/finnish-100-dev --task 1