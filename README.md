# Backend

[![Docker](https://img.shields.io/badge/-Docker-EEE.svg?logo=docker&style=flat)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python:3.10-F9DC3E.svg?logo=python&style=flat)](https://www.python.org/)
[![Django:4.x](https://img.shields.io/badge/Django:4.0-092E20.svg?logo=django&style=flat)](https://www.djangoproject.com/)
[![Nginx](https://img.shields.io/badge/-Nginx-5.svg?logo=nginx&style=flat)](https://www.nginx.co.jp/)
[![Redis](https://img.shields.io/badge/Redis:6.2-511.svg?logo=redis&style=flat)](https://redis.io/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/d-Party/d-Party-Backend/blob/main/LICENSE)

d-Party のバックエンド部分を担当するフォルダ

## 初回起動コマンド

初回は Django の migrate と collectstatic が必要になります。

従って初回起動時は以下のコマンドで実行する必要があります。

```bash
docker-compose build --no-cache
docker-compose up -d
docker-compose exec django poetry run python manage.py makemigrations
docker-compose exec django poetry run python manage.py makemigrations streamer
docker-compose exec django poetry run python manage.py migrate
docker-compose exec django poetry run python manage.py collectstatic
docker-compose down
docker-compose up -d
```

また 2 回目以降の起動であれば、`docker-compose up -d`のみで起動することができます。

## 開発

settings.py で`debug = True`においてコンテナを起動させた場合に 8000 ポートにデプロイされている Django コンテナに直接アクセスすることで、django-debug-toolbar が有効に働きます。

### 開発環境を初期化したい

開発環境を初期化したい場合以下の手順をたどってください

1. コンテナの停止(`docker-compose down`)
2. MySQL ディレクトリにある data ディレクトリを中身ごと削除する
3. Django/streamer ディレクトリにある migrations ディレクトリを中身事削除する
