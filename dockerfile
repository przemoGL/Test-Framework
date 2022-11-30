FROM python:3.11-buster

WORKDIR /Test-Framework
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "pytest" ]
CMD [ ". -s -v" ]