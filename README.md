# d-party Backend

[![Django pytest](https://github.com/d-party/d-party-Backend/actions/workflows/pytest.yml/badge.svg?branch=main&event=push)](https://github.com/d-party/d-party-Backend/actions/workflows/pytest.yml)
[![Lizard Runner](https://github.com/d-party/d-party-Backend/actions/workflows/lizard.yml/badge.svg?branch=main&event=push)](https://github.com/d-party/d-party-Backend/actions/workflows/lizard.yml)
[![SAST](https://github.com/d-party/d-party-Backend/actions/workflows/sast.yml/badge.svg?branch=main&event=push)](https://github.com/d-party/d-party-Backend/actions/workflows/sast.yml)
[![Python Auto Black](https://github.com/d-party/d-party-Backend/actions/workflows/autoblack.yml/badge.svg?branch=main&event=push)](https://github.com/d-party/d-party-Backend/actions/workflows/autoblack.yml)
[![CodeQL](https://github.com/d-party/d-party-Backend/actions/workflows/codeql-analysis.yml/badge.svg?branch=main&event=push)](https://github.com/d-party/d-party-Backend/actions/workflows/codeql-analysis.yml)

[![codecov](https://codecov.io/gh/d-party/d-party-Backend/branch/main/graph/badge.svg?token=WZ8DXWKN50)](https://codecov.io/gh/d-party/d-party-Backend)
[![Website](https://img.shields.io/website?label=d-party.net&up_message=online&url=https%3A%2F%2Fd-party.net)](https://d-party.net)
[![Security Headers](https://img.shields.io/security-headers?url=https%3A%2F%2Fd-party.net)](https://securityheaders.com/?q=https%3A%2F%2Fd-party.net&followRedirects=on)
[![Mozilla HTTP Observatory Grade](https://img.shields.io/mozilla-observatory/grade/d-party.net?publish)](https://observatory.mozilla.org/analyze/d-party.net)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/d-Party/d-Party-Backend/blob/main/LICENSE)
[![total-user](https://img.shields.io/endpoint?url=https://d-party.net/api/shields/total-user)](https://d-party.net)
[![total-room](https://img.shields.io/endpoint?url=https://d-party.net/api/shields/total-room)](https://d-party.net)

[![Docker](https://img.shields.io/badge/-Docker-EEE.svg?logo=docker&style=flat)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python:3.10-F9DC3E.svg?logo=python&style=flat)](https://www.python.org/)
[![Django:4.x](https://img.shields.io/badge/Django:4.0-092E20.svg?logo=django&style=flat)](https://www.djangoproject.com/)
[![Nginx](https://img.shields.io/badge/-Nginx-5.svg?logo=nginx&style=flat)](https://www.nginx.co.jp/)
[![Redis](https://img.shields.io/badge/Redis:6.2-511.svg?logo=redis&style=flat)](https://redis.io/)

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

### 開発環境を初期化

開発環境を初期化したい場合以下の手順をたどってください

1. コンテナの停止(`docker-compose down`)
2. MySQL ディレクトリにある data ディレクトリを中身ごと削除する
3. Django/streamer ディレクトリにある migrations ディレクトリを中身事削除する

### テストを実行

テストを実行したい場合、全てのコンテナを立ち上げてから、以下のコマンドを実行してください。

```bash
docker-compose exec django poetry run pytest --cov --workers auto
```

### cronの標準出力/エラー出力を取得

```bash
docker-compose exec django cat /var/log/cron.log
```

### その他

開発に必要な情報は出来る限り、[wiki](https://github.com/d-party/d-party-Backend/wiki)に集約しています。
適宜ご参照ください。

また、質問事項などがありましたら、[ディスカッション](https://github.com/d-party/d-party-Backend/discussions)からご連絡ください。

## 関連リンク

### リリース

- [d-party.net](https://d-party.net/)

### 拡張機能

#### ウェブストア

- [d-party - Chrome ウェブストア](https://chrome.google.com/webstore/detail/d-party/ibmlcfpijglpfbfgaleaeooebgdgcbpc)

#### リポジトリ

- [d-party/d-party-Chrome-Extensions](https://github.com/d-party/d-party-Chrome-Extensions)
