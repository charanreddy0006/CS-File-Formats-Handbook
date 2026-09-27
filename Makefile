.PHONY: validate stats search

validate:
	python scripts/validate_catalog.py

stats:
	python scripts/stats.py

search:
	python scripts/find_extension.py $(EXT)
