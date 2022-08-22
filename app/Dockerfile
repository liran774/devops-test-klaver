From python:3.8
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "./server.py"]
