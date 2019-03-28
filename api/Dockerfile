

FROM ubuntu:latest
MAINTAINER Your Name "youremail@domain.tld"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential --fix-missing
COPY . /app
WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
RUN pip --proxy=http://172.16.2.30:8080 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]