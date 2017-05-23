python3 ./scripts/oracle_candidates.py ./results/english-test.low 10 ./post-correction/task1/english-dev

encdec_models/spanish-low.1.model:all/task1/spanish-train-low all/task1/spanish-train-medium all/task1/spanish-train-high all/task1/spanish-dev all/task1/spanish-test
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.1.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.2.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.3.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.4.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.5.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.6.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.7.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.8.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.9.model
	python3 scripts/attention_train.py all/task1/spanish-train-low all/task1/spanish-dev 50 100 0.01 encdec_models/spanish-low.10.model