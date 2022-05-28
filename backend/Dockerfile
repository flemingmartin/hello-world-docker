FROM balenalib/raspberry-pi-python:3.7-buster
WORKDIR /app
RUN pip install flask
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]