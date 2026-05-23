FROM python:3.12-alpine

# Directory
WORKDIR /app

# Coprt and install requirements
COPY requirements.txt .
RUN pip install no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the Python script
CMD ["python" , "src/main.py"]