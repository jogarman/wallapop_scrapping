# No es posible correr gopro_scrapper ni iphone_scrapper
# por que todos los programas de python dependen del pwd
# El pwd es independiente para cada tarea de make y no se
# puede cambiar

# De la misma forma que no se puede hacer Play en VSCode
# a un archivo que no esté en la carpeta raiz del entorno
# de trabajo

SHELL := /c/Program\ Files/Git/usr/bin/bash.exe
folder_with_pys = build
folder_with_ipynbs = src

convert:
	@python $(folder_with_ipynbs)/convert_ipynb_to_py.py

# Tarea para Docker build
docker_build:
	@docker build -t i_gopro_v2 .

docker_run:
	@echo "No configurado"
	@docker run [volumen]:[volumen] i_gopro_v2

clean:
	@rm -rf build

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

.PHONY: gopro iphone convert docker_build docker_run clean git
# Evitar errores por argumentos posicionales
%:
	@:
