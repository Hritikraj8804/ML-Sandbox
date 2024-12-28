# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY backend/ /app/backend/
COPY frontend/templates /app/frontend/templates/
COPY frontend/static /app/frontend/static/

# Expose port and run the app
EXPOSE 5000
CMD ["python", "/app/backend/app.py"]
