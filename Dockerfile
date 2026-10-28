FROM python:3.11-slim

WORKDIR /app

COPY app.py .

# Run unbuffered so output appears immediately in terminal/logs
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]