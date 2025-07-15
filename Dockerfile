FROM python:3.10-slim
WORKDIR /app
COPY app /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]