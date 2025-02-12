# No es posible correr gopro_scrapper ni iphone_scrapper
# por que todos los programas de python dependen del pwd
# El pwd es independiente para cada tarea de make y no se
# puede cambiar

# De la misma forma que no se puede hacer Play en VSCode
# a un archivo que no esté en la carpeta raiz del entorno
# de trabajo


folder_with_pys = build
folder_with_ipynbs = src

COMMIT_MSG = $(filter-out $@,$(MAKECMDGOALS))



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
	@exit 1
endif
	@git add .
	@git commit -m "$(COMMIT_MSG)"
	@git push

.PHONY: gopro iphone convert docker_build docker_run clean git
# Evitar errores por argumentos posicionales
%:
	@:
