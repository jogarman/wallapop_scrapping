.ONESHELL:
SHELL := /usr/bin/bash

# No es posible correr gopro_scrapper ni iphone_scrapper
# por que todos los programas de python dependen del pwd
# El pwd es independiente para cada tarea de make y no se
# puede cambiar

# De la misma forma que no se puede hacer Play en VSCode
# a un archivo que no esté en la carpeta raiz del entorno
# de trabajo

folder_with_pys = build
folder_with_ipynbs = src
version = v0.1
image_name = i_gopro_$(version)
container_name = c_gopro_$(version)

COMMIT_MSG = $(filter-out $@,$(MAKECMDGOALS))

build:
	python $(folder_with_ipynbs)/convert_ipynb_to_py.py

# Tarea para Docker build
build_docker:
	docker build -t $(image_name) .
run_docker:
	docker run --name $(container_name) -v "C:/Users/ACER/Desktop/Proyectos python/wallapop_scrapping/volumen_host:/app/data/3_feature_engineering" $(image_name)

git:
ifndef msg
	@echo "Usage: make git msg=\"commit message\""
	@exit 1
endif
	git config --global user.email "122149837+jogarman@users.noreply.github.com"
		git config --global user.name "jogarman"
	@git add .
	@git commit -m "$(msg)"
	@git push

clean:
	@rm -rf build

.PHONY: *
# Evitar errores por argumentos posicionales
%:
	@:
