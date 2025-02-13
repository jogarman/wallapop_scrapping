# Use the official Python image from the Docker Hub
FROM python:3.11.9

RUN apt-get update 
RUN apt-get install -y build-essential
RUN apt-get install -y --no-install-recommends chromium

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements_docker.txt

# Create the required directories
RUN mkdir -p \
	/app/data/1_datos_raw \
	/app/data/2_datos_por_fecha \
	/app/data/3_feature_engineering
	# /app/4_download_description \
	# /app/5_data_from_comments

# Run app.py when the container launches

WORKDIR /app/build
CMD ["python", "gopro_scrapper.py"]