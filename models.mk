DATADIR=all/task1
SCRIPTS=scripts
ENCDEC_RESULTS=encdec_results
ENCDEC_MODELS=encdec_models
EVAL=evaluation
PYTHON=python3

%-encdec-eval:encdec_results/%-test.low.1.sys
	python3 evaluation/evalm.py --gold all/task1/finnish-dev --guess encdec_results/finnish-test.low.sys --task 1

.PRECIOUS:%.model %.sys

encdec_models/finnish-low.1.model:all/task1/finnish-train-low all/task1/finnish-train-medium all/task1/finnish-train-high all/task1/finnish-dev all/task1/finnish-test
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.1.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.2.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.3.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.4.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.5.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.6.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.7.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.8.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.9.model
	python3 scripts/attention_train.py all/task1/finnish-train-low all/task1/finnish-dev 50 100 0.01 encdec_models/finnish-low.10.model