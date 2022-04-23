# Django Container

[![Python](https://img.shields.io/badge/Python:3.10-F9DC3E.svg?logo=python&style=flat)](https://www.python.org/)
[![Django:4.x](https://img.shields.io/badge/Django:4.0-092E20.svg?logo=django&style=flat)](https://www.djangoproject.com/)

## intro

このコンテナはウェブアプリケーションサーバーとして動作します。

## アプリ構成

Djangoのアプリケーションは以下のような構造になっています。

### web

静的ファイル全般を扱うアプリ

### streamer

非同期通信を行うコンポーネント全般を扱うアプリ
[Django Channels](https://channels.readthedocs.io/en/stable/)及び[Django Channels Rest Framework](https://djangochannelsrestframework.readthedocs.io/en/latest/)によって構築

### api

APIエンドポイントを定義するためのアプリ
バージョンチェックAPIなどに使用

[Django REST framework](https://www.django-rest-framework.org/)によって構築

## library

### primary library

- [Django : 4.0](https://www.djangoproject.com/)
- [Django Channels : 3.0.4](https://channels.readthedocs.io/en/stable/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Gunicorn](https://gunicorn.org/)
- [Uvicorn](https://www.uvicorn.org/)

### utils library

- [Django Channels Rest Framework](https://djangochannelsrestframework.readthedocs.io/en/latest/)
- [Jazzmin](https://django-jazzmin.readthedocs.io/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [django-boost 2.0](https://django-boost.readthedocs.io/en/latest/)

### develop library

- [pytest](https://docs.pytest.org/en/7.0.x/)
- [Black](https://black.readthedocs.io/en/stable/)
