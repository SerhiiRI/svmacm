.PHONY: clean-pyc clean-build docs clean

BROWSER := python -c "$$BROWSER_PYSCRIPT"


python	= /usr/bin/python3


help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

clean: clean-build clean-pyc clean-test

install:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 leviathan_serving tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source leviathan_serving setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs:
	rm -f docs/leviathan_serving.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ leviathan_serving
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

REPO_SCM_DIRECTORY = $(shell pwd)
REPO_SCM_SERVICE_PATH = $(shell pwd)/service/

SCM_SERVICE_NAME = scm-server.service
SCM_SOCKET_NAME = scm-server.socket

DIR_LINUX_PROGRAM_LOCATION = /usr/local/etc/scm/
DIR_LINUX_SYSTEMD_PATH = /etc/systemd/system/

SCM_SYSTEMD_SERVICE_PATH = $(DIR_LINUX_SYSTEMD_PATH)$(SCM_SERVICE_NAME)

install: clean
	@if [ "$(id -u)" != "0" ]; then 
	@echo "This script must be run as root" 1>&2 
	@exit 1 
	@fi
	@if [ ! -f  ];
	cp $(REPO_SCM_SERVICE_PATH)$(SCM_SERVICE_NAME) $(SCM_SYSTEMD_SERVICE_PATH)
	cp $(REPO_SCM_SERVICE_PATH)$(SCM_SOCKET_NAME) $(SCM_SYSTEMD_SERVICE_PATH)
	cp -avr $(SCM_DIRECTORY)* $(DIR_LINUX_PROGRAM_LOCATION)
	@systemctl enable $(SCM_SERVICE_NAME)
	@systemctl start $(SCM_SERVICE_NAME)


python setup.py install

config:

remove:

run-local:


OBJFILES 	= loader.o \
						common/printf.o \
						common/screen.o	\
						common/interrupt.o \
						common/descriptor_tables.o \
						common/isr.o \
						common/gdt.o \
						common/memory.o \
						common/PCI/pci.o \
						common/devices/keyboard.o \
						common/devices/timer.o \
						common/stdlib/paging.o \
						common/stdlib/kernelheap.o \
						common/stdlib/ordered_array.o \
						common/stdlib/task.o \
						common/stdlib/process.o \
						kernel.o

all: kernel.bin
rebuild: clean all

image: kernel.bin
					@echo -e "\033[92mCreating image \033[1mDuckOS.img\033[0m"
					@cp ./kernel.bin ./img/boot/
					@grub2-mkrescue -o duck.img img

cleanimage:
					@rm -f ./img/boot/kernel.bin

loader.o: loader.s
				$(AS) $(ASFLAGS) -o $@ $<

common/interrupt.o: common/interrupt.s
				$(AS) $(ASFLAGS) -o $@ $<

common/gdt.o: common/gdt.s
				$(AS) $(ASFLAGS) -o $@ $<

common/stdlib/process.s: common/stdlib/process.s
				$(AS) $(ASFLAGS) -o $@ $<

.c.o:
				$(CC) -Iinclude $(CFLAGS) -o $@ -c $<

kernel.bin: $(OBJFILES)
				$(LD) $(LDFLAGS) -T linker.ld -o $@ $^
				cp $@ $@.gdb
				strip $@

clean:
				@rm -f $(OBJFILES)


