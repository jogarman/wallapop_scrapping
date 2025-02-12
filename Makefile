# Variables (por defecto, vacío)
COMMIT_MSG = $(msg)

# Tarea para git commit y push
git:
ifndef msg
	@echo "Error: Debes proporcionar un mensaje de commit. Usa: make git_commit_push msg='tu mensaje'"
	exit 1
endif
	git add .
	git commit -m "$(COMMIT_MSG)"
	git push

# Tarea para Docker build
docker_build:
	docker build -t i_gopro_v2 .
docker_run:
	echo "no configurado"
	docker run [volumen]:[volumen] i_gopro_v2
# Tarea para ejecutar Python
convert:
	python dist/convert_ipynb_to_py.py
