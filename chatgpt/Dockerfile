FROM python:3.9.16-bullseye

RUN apt update && apt upgrade -y
RUN apt install -y rsync gcc python3-dev \
    libmariadb-dev mariadb-common

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait
RUN chmod +x /wait

RUN pip3 install pipenv && rm -rf ~/.cache
WORKDIR /code/
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --dev --system && rm -rf ~/.cache/
COPY manage.py ./

CMD /wait && python3 ./manage.py runserver 0.0.0.0:8000