FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 启动 Django（0.0.0.0:8000 允许外部访问容器）
CMD ["python", "app.py", "runserver", "0.0.0.0:8000"]
