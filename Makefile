SERVICE = uiservice
SERVICE_CAPS = UIService
SPEC_FILE = UIService.spec
URL = https://kbase.us/services/uiservice
DIR = $(shell pwd)
LIB_DIR = lib
SCRIPTS_DIR = scripts
TEST_DIR = test
LBIN_DIR = bin
EXECUTABLE_SCRIPT_NAME = run_$(SERVICE_CAPS)_async_job.sh
STARTUP_SCRIPT_NAME = start_server.sh
TEST_SCRIPT_NAME = run_tests.sh
MODULE_USER = kbmodule

.PHONY: test

default: compile

install: compile build build-startup-script build-executable-script build-test-script

all: build build-startup-script build-executable-script build-test-script

test-all: build build-startup-script build-executable-script build-test-script

compile:
	@bash scripts/compile.bash $(SERVICE_CAPS) $(SPEC_FILE) $(LIB_DIR)

build:
	@chmod +x $(SCRIPTS_DIR)/entrypoint.sh

build-executable-script:
	@mkdir -p $(LBIN_DIR)
	@echo '#!/bin/bash' > $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	@echo 'script_dir=$$(dirname "$$(readlink -f "$$0")")' >> $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	@echo 'export PYTHONPATH=$$script_dir/../$(LIB_DIR):$$PATH:$$PYTHONPATH' >> $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	@echo 'python -u $$script_dir/../$(LIB_DIR)/$(SERVICE_CAPS)/$(SERVICE_CAPS)Server.py $$1 $$2 $$3' >> $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	@chmod +x $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)

build-startup-script:
	@mkdir -p $(LBIN_DIR)
	@echo '#!/bin/bash' > $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)
	@echo 'script_dir=$$(dirname "$$(readlink -f "$$0")")' >> $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)
	@echo 'export KB_DEPLOYMENT_CONFIG=$$script_dir/../deploy.cfg' >> $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)
	@echo 'export PYTHONPATH=$$script_dir/../$(LIB_DIR):$$PATH:$$PYTHONPATH' >> $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)
	@echo 'uwsgi --master --processes 5 --threads 5 --http :5000 --uid $$(id -u kbmodule) --gid $$(id -g kbmodule)  --wsgi-file $$script_dir/../$(LIB_DIR)/$(SERVICE_CAPS)/$(SERVICE_CAPS)Server.py' >> $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)
	@chmod +x $(SCRIPTS_DIR)/$(STARTUP_SCRIPT_NAME)

build-test-script:
	@echo '#!/bin/bash' > $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'script_dir=$$(dirname "$$(readlink -f "$$0")")' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'export KB_DEPLOYMENT_CONFIG=$$script_dir/../deploy.cfg' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'export KB_AUTH_TOKEN=`cat /kb/module/work/token`' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'export PYTHONPATH=$$script_dir/../$(LIB_DIR):$$PATH:$$PYTHONPATH' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'cd $$script_dir/../$(TEST_DIR)' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'echo "Running tests"' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'echo `pwd`' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@echo 'python -m nose --with-coverage --cover-package=$(SERVICE_CAPS) --cover-html --cover-html-dir=/kb/module/work/test_coverage --nocapture  --nologcapture --cover-config-file=$$script_dir/../$(TEST_DIR)/coverage.cfg .' >> $(TEST_DIR)/$(TEST_SCRIPT_NAME)
	@chmod +x $(TEST_DIR)/$(TEST_SCRIPT_NAME)

docker-image-dev:
	@echo "> Creating local image for development or testing"
	@bash scripts/build-docker-image-dev.sh	

run-docker-image-dev:
	@echo "> Running the already-built docker image"
	@bash scripts/run-docker-image-dev.sh	

test:
	@if [ ! -f /kb/module/work/token ]; then echo -e '\nOutside a docker container please run "kb-sdk test" rather than "make test"\n' && exit 1; fi
	@bash $(TEST_DIR)/$(TEST_SCRIPT_NAME)

clean:
	@rm -rfv $(LBIN_DIR)
