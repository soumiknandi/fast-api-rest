# Build stage
FROM python:3.12-slim AS build

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \ 
gcc \
libpq-dev
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Copy application code
COPY . . 

# Expose port
EXPOSE 8000

# Set the entrypoint
CMD ["fastapi", "run"] 