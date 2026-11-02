.PHONY: test audit registry ingest-check
test:
	python -m pytest tests/ -q || python -m unittest discover -s tests -v
audit:
	python3 scripts/audit_repo.py
registry:
	python3 scripts/build_registry.py
ingest-check:
	python3 scripts/ingest_daily.py --ids 2507.17049 --primary-doc evaluation-and-benchmarks.md --dirs R36 --obs V0 --sup L1 --verdict "dry-run check" --cannot-prove "dry-run" --dry-run
