FROM ubuntu:22.04

RUN apt-get update; apt-get install -y python3; apt-get install -y pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
