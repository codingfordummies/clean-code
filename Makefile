venv: dev-requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur dev-requirements.txt
	# ./venv/bin/pip install -Ur docs/requirements.txt
	touch venv

.PHONY: setup_versioneer
setup_versioneer: venv
	./venv/bin/versioneer install
