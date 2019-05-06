# Makefile for es Python Documentation
#
# Here is what you can do:
#
# - make  # Automatically build an html local version
# - make todo  # To list remaining tasks
# - make merge  # To merge pot from upstream
# - make fuzzy  # To find fuzzy strings
# - make progress  # To compute current progression
# - make upgrade_venv  # To upgrade the venv that compiles the doc
#
# Modes are: autobuild-stable, autobuild-dev, and autobuild-html,
# documented in gen/src/3.6/Doc/Makefile as we're only delegating the
# real work to the Python Doc Makefile.

CPYTHON_CLONE := ../cpython/
SPHINX_CONF := $(CPYTHON_CLONE)/Doc/conf.py
LANGUAGE := es
VENV := ~/.venvs/python-docs-i18n/
PYTHON := $(shell which python3)
MODE := html
BRANCH = 3.7
COMMIT =
JOBS = auto


.PHONY: all
all: $(SPHINX_CONF) $(VENV)/bin/activate
ifneq "$(shell cd $(CPYTHON_CLONE) 2>/dev/null && git describe --contains --all HEAD)" "$(BRANCH)"
	$(warning "Your ../cpython checkout may be on the wrong branch, got $(shell cd $(CPYTHON_CLONE) 2>/dev/null && git describe --contains --all HEAD) expected $(BRANCH)")
endif
	mkdir -p $(CPYTHON_CLONE)/locales/$(LANGUAGE)/
	ln -nfs $(shell $(PYTHON) -c 'import os; print(os.path.realpath("."))') $(CPYTHON_CLONE)/locales/$(LANGUAGE)/LC_MESSAGES
	$(MAKE) -C $(CPYTHON_CLONE)/Doc/ VENVDIR=$(VENV) PYTHON=$(PYTHON) SPHINXOPTS='-qW -j$(JOBS) -D locale_dirs=../locales -D language=$(LANGUAGE) -D gettext_compact=0 -D latex_engine=xelatex -D latex_elements.inputenc= -D latex_elements.fontenc=' $(MODE)


$(SPHINX_CONF):
	git clone --depth 1 --branch $(BRANCH) https://github.com/python/cpython.git $(CPYTHON_CLONE)
	[ -n "$(COMMIT)" ] && (i=1; while ! $$(git -C $(CPYTHON_CLONE) checkout $(COMMIT)); do i=$$((i * 2)); git -C $(CPYTHON_CLONE) fetch --depth $$i; done) || true


.PHONY: upgrade_venv
upgrade_venv:
	$(MAKE) -C $(CPYTHON_CLONE)/Doc/ VENVDIR=$(VENV) PYTHON=$(PYTHON) venv


$(VENV)/bin/activate:
	$(MAKE) -C $(CPYTHON_CLONE)/Doc/ VENVDIR=$(VENV) PYTHON=$(PYTHON) venv


.PHONY: progress
progress:
	@python3 -c 'import sys; print("{:.1%}".format(int(sys.argv[1]) / int(sys.argv[2])))'  \
	$(shell msgcat *.po */*.po | msgattrib --translated | grep -c '^msgid') \
	$(shell msgcat *.po */*.po | grep -c '^msgid')


.PHONY: merge
merge: upgrade_venv
ifneq "$(shell cd $(CPYTHON_CLONE) 2>/dev/null && git describe --contains --all HEAD)" "$(BRANCH)"
	$(error "You're merging from a different branch:" "$(shell cd $(CPYTHON_CLONE) 2>/dev/null && git describe --contains --all HEAD)" vs "$(BRANCH)")
endif
	(cd $(CPYTHON_CLONE)/Doc; rm -f build/NEWS)
	(cd $(CPYTHON_CLONE); $(VENV)/bin/sphinx-build -Q -b gettext -D gettext_compact=0 Doc pot/)
	find $(CPYTHON_CLONE)/pot/ -name '*.pot' |\
	    while read -r POT;\
	    do\
	        PO="./$$(echo "$$POT" | sed "s#$(CPYTHON_CLONE)/pot/##; s#\.pot\$$#.po#")";\
	        mkdir -p "$$(dirname "$$PO")";\
	        if [ -f "$$PO" ];\
	        then\
	            case "$$POT" in\
	            *whatsnew*) msgmerge --backup=off --force-po --no-fuzzy-matching -U "$$PO" "$$POT" ;;\
	            *)          msgmerge --backup=off --force-po -U "$$PO" "$$POT" ;;\
	            esac\
	        else\
	            msgcat -o "$$PO" "$$POT";\
	        fi\
	    done


.PHONY: fuzzy
fuzzy:
	for file in *.po */*.po; do echo $$(msgattrib --only-fuzzy --no-obsolete "$$file" | grep -c '#, fuzzy') $$file; done | grep -v ^0 | sort -gr
