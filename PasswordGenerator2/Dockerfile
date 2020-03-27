FROM python:3.6
WORKDIR /PasswordGenerator2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
