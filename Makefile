DOCS_DIR=$(PWD)/docs
DOCS_SOURCE_FILES:= $(shell find $(DOCS_DIR) -type f -name "*.rst" -print)

SRC_DIR=$(PWD)/src/clean_code

COMPILE_READING_LIST_SCRIPT=$(SRC_DIR)/compile_reading_list.py
READING_LIST_SOURCE_FILES:= $(shell find $(DOCS_DIR)/reading -type f -name "*.yml" -print)


$(DOCS_DIR)/reading_list.rst: $(COMPILE_READING_LIST_SCRIPT) venv $(READING_LIST_SOURCE_FILES) $(DOCS_DIR)/reading_list_template.rst
	./venv/bin/python $(COMPILE_READING_LIST_SCRIPT)

.PHONY: docs
docs:
	make $(DOCS_DIR)/_build/html/index.html

# Have to run build twice to get stuff in right place
$(DOCS_DIR)/_build/html/index.html: $(DOCS_DIR)/*.py $(DOCS_DIR)/_templates/*.html $(DOCS_SOURCE_FILES) src/clean_code/*.py README.rst venv
	source ./venv/bin/activate; cd $(DOCS_DIR); make html

venv: dev-requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur dev-requirements.txt
	# ./venv/bin/pip install -Ur docs/requirements.txt
	./venv/bin/pip install -e .[test]
	touch venv

.PHONY: setup_versioneer
setup_versioneer: venv
	./venv/bin/versioneer install

.PHONY: variables
variables:
	@echo DOCS_DIR: $(DOCS_DIR)
	@echo DOCS_SOURCE_FILES: $(DOCS_SOURCE_FILES)

	@echo SRC_DIR: $(SRC_DIR)

	@echo COMPILE_READING_LIST_SCRIPT: $(COMPILE_READING_LIST_SCRIPT)
	@echo READING_LIST_SOURCE_FILES: $(READING_LIST_SOURCE_FILES)
