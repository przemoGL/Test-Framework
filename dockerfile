# docker build . -t Test-Framework
# docker run Test-Framework:latest

FROM python:3.11-buster

WORKDIR /Test-Framework

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "pytest" ]
CMD [ ". -s -v" ]