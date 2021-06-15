EXISTS:=$(shell command -v python 2> /dev/null | wc -l)
NAME:=$(shell cat /etc/*release | grep "^NAME=" | cut --delimiter="=" -f 2)
CURRENT_DIR = $(shell pwd)
.ONESHELL:
SHELL := /bin/bash

PROJECT:="plandarm"

all: check-pyhton initialize activate pull migrate
	@echo "Ready to go"

check-pyhton:
ifeq ($(EXISTS), 1)
	@echo "Python installed"	
else

ifeq ($(NAME), $(filter $(NAME),"Arch Linux" "Manjaro Linux"))
	@echo "Using pacman"
	sudo pacman -S python	
endif

ifeq ($(NAME), $(filter $(NAME),"Debian" "Ubuntu" "Linux Mint"))
	@echo "Using apt"
	sudo apt install python
endif

endif

#----------venv_setup----------
initialize:
	python -m venv .venv
	
activate: 
	source $(CURRENT_DIR)/.venv/bin/activate
	
pull: activate
	pip install -r requirements.txt

#----------migrate----------
migrate:
	python $(CURRENT_DIR)/$(PROJECT)/manage.py migrate
