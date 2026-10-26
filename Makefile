PYTHON ?= python3
.PHONY: qr check pdf print site build serve clean
qr:
	$(PYTHON) scripts/generate_contribute_qr.py
check: qr
	$(PYTHON) scripts/generate_medications.py
	$(PYTHON) scripts/check.py
pdf: qr
	$(PYTHON) scripts/build_book.py --output build/survivor-guide.pdf --format screen
	mkdir -p docs/downloads
	cp build/survivor-guide.pdf docs/downloads/survivor-guide.pdf
print: qr
	$(PYTHON) scripts/build_book.py --output build/survivor-guide-print-interior.pdf --format print
site: qr
	$(PYTHON) -m mkdocs build --clean --strict
build: check pdf site
serve: qr
	$(PYTHON) -m mkdocs serve
clean:
	rm -rf build/ site/ docs/downloads/*.pdf
