FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/backend/
COPY frontend/templates /app/frontend/templates/
COPY frontend/static /app/frontend/static/

CMD ["python", "/app/backend/app.py"]
