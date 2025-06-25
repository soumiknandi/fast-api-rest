# Stage 1 -Build stage
FROM python:3.12-slim AS builder

# App working dir
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \ 
    gcc \
    libpq-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 


# Stage 2 - Runtime
FROM python:3.12-slim

# App working dir
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \ 
    gcc \
    libpq-dev

# Copy system-wide site-packages and binaries
COPY --from=builder /usr/local /usr/local
COPY . .

# Expose port
EXPOSE 8000

# Set the entrypoint
CMD ["fastapi", "run"] 