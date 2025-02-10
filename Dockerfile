# Use the official Python image from the Docker Hub
FROM python:3.11.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create the required directories
RUN mkdir -p \
	/app/1_datos_raw \
	/app/2_datos_por_fecha \
	/app/3_feature_engineering
	# /app/4_download_description \
	# /app/5_data_from_comments

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "/app/program/gopro_scrapper.py"]