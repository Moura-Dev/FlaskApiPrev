FROM fnndsc/ubuntu-python3

RUN mkdir /api

WORKDIR /api

RUN apt update

RUN apt install -y libmysqlclient-dev

COPY requirements.txt /api/

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /api/

RUN chmod +x entry-point.sh

ENTRYPOINT ["./entry-point.sh"]