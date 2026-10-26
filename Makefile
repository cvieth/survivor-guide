PYTHON ?= python3
.PHONY: qr images check pdf print site build serve clean
qr:
	$(PYTHON) scripts/generate_contribute_qr.py

images:
	$(PYTHON) scripts/fetch_herbal_plates.py
check: qr images
	$(PYTHON) scripts/generate_medications.py
	$(PYTHON) scripts/check.py
pdf: qr images
	$(PYTHON) scripts/build_book.py --output build/survivor-guide.pdf --format screen
	mkdir -p docs/downloads
	cp build/survivor-guide.pdf docs/downloads/survivor-guide.pdf
print: qr images
	$(PYTHON) scripts/build_book.py --output build/survivor-guide-print-interior.pdf --format print
site: qr images
	$(PYTHON) -m mkdocs build --clean --strict
build: check pdf site
serve: qr images
	$(PYTHON) -m mkdocs serve
clean:
	rm -rf build/ site/ docs/downloads/*.pdf
