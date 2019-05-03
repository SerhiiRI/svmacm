SHELL := /bin/bash
python	= /usr/bin/python3
SCM_SERVICE_NAME = scm-server.service
REPO_SCM_DIRECTORY = $(shell pwd)
REPO_SCM_SERVICE_PATH = $(shell pwd)/service/
DIR_LINUX_PROGRAM_LOCATION = /usr/local/etc/scm/
DIR_LINUX_SYSTEMD_PATH = /etc/systemd/system/
SCM_SYSTEMD_SERVICE_PATH = $(DIR_LINUX_SYSTEMD_PATH)$(SCM_SERVICE_NAME)

# COLORS
CYAN=\033[96m\033[1m
GREEN=\033[32m\033[1m
RED=\033[31m\033[1m
NC=\033[0m
BOLD = \033[1m

help:
	@echo "Name:"
	@echo -e "\t${GREEN}Simple Container Manager(SCM)${NC}"
	@echo -e "\nDescribe:"
	@echo -e "\tSCM is a simple program to monitoring and control\n\tdocker virutal machines and images which can\n\twork with JSON api or web grafical interface"
	@echo -e "\nCommands:"
	@echo -e "\tinstall\t- install program and run on port 8777"
	@echo -e "\trunloc\t- just up the server on port 8777"
	@echo -e "\tkill\t- kill server matherfucka"
	@echo -e "\tremove\t- remove all files"
	@echo -e "\thelp\t- print this message"

remove:
	@if [ $(shell id -u) -ne 0 ]; then \
	echo -e "[${RED}Error${NC}] This script must be run as root" 1>&2; \
	exit 1; \
	fi;

	@if [ "$(shell systemctl is-active scm-server)" = "active" ]; then \
	systemctl --quiet stop scm-server; \
	echo -e "[${GREEN}Success${NC}] stop 'scm-server' service"; \
	systemctl --quiet disable scm-server; \
	echo -e "[${GREEN}Success${NC}] unregister 'scm-server' service "; \
	systemctl --quiet daemon-reload; \
	echo -e "[${CYAN}info${NC}] reload daemons "; \
	fi;
	@if [ -d $(DIR_LINUX_PROGRAM_LOCATION) ]; then \
	rm -rf $(DIR_LINUX_PROGRAM_LOCATION); \
	echo -e "[${GREEN}Success${NC}] deleted program path in $(DIR_LINUX_PROGRAM_LOCATION)"; \
	fi;
	@if [ -e $(SCM_SYSTEMD_SERVICE_PATH) ]; then \
	rm -f $(SCM_SYSTEMD_SERVICE_PATH); \
	echo -e "[${GREEN}Success${NC}] systemd UNIT service file successfuly removed"; \
	fi;
	@echo -e "[${GREEN}Success${NC}] SCM removed from this computer "


install:
	@if [ $(shell id -u) -ne 0 ]; then echo -e "[${RED}Error${NC}] This script must be run as root" 1>&2; exit 1; fi;
	@if [ ! -d  $(DIR_LINUX_PROGRAM_LOCATION) ]; \
	then mkdir -p $(DIR_LINUX_PROGRAM_LOCATION); \
	echo -e "[${GREEN}Success${NC}] created program path in directory $(DIR_LINUX_PROGRAM_LOCATION)"; \
	else echo -e "[${CYAN}info${NC}] folder $(DIR_LINUX_PROGRAM_LOCATION) exist"; \
	fi;

	@if [ ! -d  $(DIR_LINUX_SYSTEMD_PATH) ]; \
	then mkdir -p $(DIR_LINUX_SYSTEMD_PATH); \
	echo -e "[${GREEN}Success${NC}] created SYSTEMD path in $(DIR_LINUX_SYSTEMD_PATH)";  \
	else echo -e "[${CYAN}info${NC}] the catalog $(DIR_LINUX_SYSTEMD_PATH) exist"; \
	fi;

	@echo -e "[${GREEN}Success${NC}] maked needed file hierarchy"
	@cp $(REPO_SCM_SERVICE_PATH)$(SCM_SERVICE_NAME) $(SCM_SYSTEMD_SERVICE_PATH)
	@cp -avr $(SCM_DIRECTORY)* $(DIR_LINUX_PROGRAM_LOCATION)
	@echo -e "[${GREEN}Success${NC}] moved program to location"
	@systemctl enable scm-server
	@systemctl start scm-server
	@echo -e "[${GREEN}Success${NC}] started systemd service"

runloc:
	@if [ $(shell id -u) -ne 0 ]; then echo -e "[${RED}Error${NC}] This script must be run as root" 1>&2; exit 1; fi
	@if [ "$(shell /usr/bin/python3 service/test_port.py)" -eq "0" ] ; then \
	/usr/bin/python3 scm.py &>/dev/null & \
	echo -e "[${GREEN}Success${NC}] service run with pid "$(shell pgrep scm.py); \
	else \
	echo -e "[${RED}Error${NC}] port is already used motherfucka"; \
	fi;

kill:
	@if [ $(shell id -u) -ne 0 ]; then echo -e "[${RED}Error${NC}] This script must be run as root" 1>&2; exit 1; fi

	@if [ "$(shell systemctl is-active scm-server)" = "active" ]; then \
	systemctl --quiet stop scm-server; \
	echo -e "[${GREEN}Success${NC}] server stoped"; \
	else \
	if [ ! -z "$(shell pgrep scm.py)" ] && [ -n $(shell pgrep scm.py) ] && [ $(shell pgrep scm.py) -eq $(shell pgrep scm.py) ]  2>/dev/null; then \
	kill $(shell pgrep scm.py); \
	echo -e "[${GREEN}Success${NC}] server killed"; \
	else \
	echo -e "[${RED}Error${NC}]: PID does not exist" >&2; exit 1; \
	fi; \
	fi;
