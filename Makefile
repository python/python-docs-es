#
# Makefile for Spanish Python Documentation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  based on: https://github.com/python/python-docs-pt-br/blob/3.8/Makefile
#

# Configuration

CPYTHON_PATH        := cpython   #Current commit for this upstream repo is setted by the submodule
BRANCH              := 3.8
LANGUAGE_TEAM       := python-docs-es
LANGUAGE            := es

# Internal variables
VENV                := $(shell realpath ./venv)
PYTHON              := $(shell which python3)
CPYTHON_WORKDIR     := cpython
OUTPUT_DOCTREE      := $(CPYTHON_WORKDIR)/Doc/_build/doctree
OUTPUT_HTML      := $(CPYTHON_WORKDIR)/Doc/_build/html
LOCALE_DIR          := $(CPYTHON_WORKDIR)/locale
TRANSIFEX_PROJECT   := python-docs-es
POSPELL_TMP_DIR     := .pospell


.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo " build        Build an local version in html, with warnings as errors"
	@echo " serve        Serve a built documentation on http://localhost:8000"
	@echo " spell        Check spelling"
	@echo " wrap         Wrap all the PO files to a fixed column width"
	@echo " progress     To compute current progression on the tutorial"
	@echo " dict_dups	Check duplicated entries on the dict"
	@echo ""


# build: build the documentation using the translation files currently available
#        at the moment. For most up-to-date docs, run "tx-config" and "pull"
#        before this. If passing SPHINXERRORHANDLING='', warnings will not be
#        treated as errors, which is good to skip simple Sphinx syntax mistakes.
.PHONY: build
build: setup
		PYTHONWARNINGS=ignore::FutureWarning $(VENV)/bin/sphinx-build -j auto -W --keep-going -b html -d $(OUTPUT_DOCTREE) -D language=$(LANGUAGE) . $(OUTPUT_HTML) && \
		@echo "Success! Open file://`pwd`/$(OUTPUT_HTML)/index.html, " \
					"or run 'make serve' to see them in http://localhost:8000";


# setup: After running "venv" target, prepare that virtual environment with
#        a local clone of cpython repository and the translation files.
#        If the directories exists, only update the cpython repository and
#        the translation files copy which could have new/updated files.
.PHONY: setup
setup: venv
	git submodule sync
	git submodule update --init --force $(CPYTHON_PATH)


# venv: create a virtual environment which will be used by almost every
#       other target of this script
.PHONY: venv
venv:
	if [ ! -d $(VENV) ]; then                                          \
		$(PYTHON) -m venv --prompt $(LANGUAGE_TEAM) $(VENV);             \
	fi

	$(VENV)/bin/python -m pip install -q -r requirements.txt


# serve: serve the documentation in a simple local web server, using cpython
#        Makefile's "serve" target. Run "build" before using this target.
.PHONY: serve
serve:
	$(MAKE) -C $(CPYTHON_WORKDIR)/Doc serve


# clean: remove all .mo files and the venv directory that may exist and
#        could have been created by the actions in other targets of this script
.PHONY: clean
clean:
	rm -fr $(VENV)
	rm -rf $(POSPELL_TMP_DIR)
	find -name '*.mo' -delete

.PHONY: progress
progress: venv
	$(VENV)/bin/potodo --offline --path tutorial/


.PHONY: spell
spell: venv
	# 'cat' tenia el problema que algunos archivos no tenían una nueva línea al final
	# 'awk 1' agregará una nueva línea en caso que falte.
	awk 1 dict dictionaries/*.txt > dict.txt
	$(VENV)/bin/pospell -p dict.txt -l es_ES **/*.po


.PHONY: wrap
wrap: venv
	$(VENV)/bin/powrap **/*.po

.PHONY: dict_dups
SHELL:=/bin/bash
.ONESHELL:
dict_dups:
	if [[ $$(cat dict| sort | uniq -dc) ]]; then
		echo -e "\n #######################\n"
		echo "duplicated lines in the dict file"
		sort dict | uniq -dc |sort -h
		exit 1
	else
		echo "no duplicated lines"
		exit 0
	fi
