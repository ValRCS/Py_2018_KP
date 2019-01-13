ROOT_DIR = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SCRIPT_DIR = $(ROOT_DIR)/scripts/make
INSTALL_SCRIPT = $(SCRIPT_DIR)/INSTALL
TEST_SCRIPT = $(SCRIPT_DIR)/TEST
DOC_SCRIPT = $(SCRIPT_DIR)/DOC
CLEAN_SCRIPT = $(SCRIPT_DIR)/CLEAN

.PHONY: install test help docs clean all

all: help

install:
	@$(INSTALL_SCRIPT)

test:
	@$(TEST_SCRIPT) ${TEST_TYPE}

docs:
	@$(DOC_SCRIPT)

clean:
	@$(CLEAN_SCRIPT)

help:
	@echo "Make targets:"
	@echo "install       install the project"
	@echo "test          run tests"
	@echo "docs          generate documentation"
	@echo "help          show this help"
