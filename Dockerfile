FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY requirements.txt .

RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install make \
	&& pip3 install -r requirements.txt

COPY . .

RUN addgroup --system userapp \
	&& adduser --system userapp \
	&& adduser userapp userapp \
	&& chown -R userapp:userapp .

USER userapp

ENTRYPOINT ["make", "test"]
