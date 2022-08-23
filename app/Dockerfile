From python:3.8
WORKDIR /usr/src/app
COPY app/requirements.txt ./
RUN pip install -r requirements.txt
COPY app/ .
EXPOSE 3000
CMD ["python", "./server.py"]
