FROM python:3.6
WORKDIR /RandNumGen
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
COPY . .
