# Get the Python image

# Set the working directory
WORKDIR 

# Copy reqs file to the containers
COPY requirements.txt .

# Install dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Exposing on port 6000
EXPOSE 6000

# Command to run the application
CMD ["python", "main.py"]