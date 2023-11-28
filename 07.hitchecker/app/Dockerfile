FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install flask redis
CMD ["python", "app.py"]
