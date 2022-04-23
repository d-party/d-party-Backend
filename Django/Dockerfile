FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /usr/src/app

COPY Django/.env.django /env_files/
COPY ../.env.global /env_files/

# 環境変数を設定
ENV PYTHONPATH /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBCONF_NOWARNINGS yes

RUN pip install poetry
ADD Django/pyproject.toml /usr/src/app
RUN poetry install --no-root

RUN apt-get update
RUN apt-get install -y graphviz cron
