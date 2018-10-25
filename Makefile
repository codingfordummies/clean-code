DOCS_DIR=$(PWD)/docs
DOCS_SOURCE_FILES:= $(shell find $(DOCS_DIR) -type f -name "*.rst" -print)


venv: dev-requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur dev-requirements.txt
	# ./venv/bin/pip install -Ur docs/requirements.txt
	./venv/bin/pip install -e .
	touch venv

.PHONY: setup_versioneer
setup_versioneer: venv
	./venv/bin/versioneer install

.PHONY: docs
docs:
	make $(DOCS_DIR)/_build/html/index.html

# Have to run build twice to get stuff in right place
$(DOCS_DIR)/_build/html/index.html: $(DOCS_DIR)/*.py $(DOCS_DIR)/_templates/*.html $(DOCS_SOURCE_FILES) src/clean_code/*.py README.rst
	cd $(DOCS_DIR); make html

.PHONY: variables
variables:
	@echo DOCS_DIR: $(DOCS_DIR)
	@echo DOCS_SOURCE_FILES: $(DOCS_SOURCE_FILES)
