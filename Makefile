PYTHON ?= python3
.PHONY: check pdf print site build serve clean
check:
	$(PYTHON) scripts/check.py
pdf:
	$(PYTHON) scripts/build_book.py --output build/survivor-guide.pdf --format screen
	mkdir -p docs/downloads
	cp build/survivor-guide.pdf docs/downloads/survivor-guide.pdf
print:
	$(PYTHON) scripts/build_book.py --output build/survivor-guide-print-interior.pdf --format print
site:
	$(PYTHON) -m mkdocs build --clean --strict
build: check pdf site
serve:
	$(PYTHON) -m mkdocs serve
clean:
	rm -rf build/ site/ docs/downloads/*.pdf
