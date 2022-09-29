FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
ENV PYTHONPATH /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBCONF_NOWARNINGS yes

# 必須ソフトウェアのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends graphviz cron && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

# poetry環境構築
RUN pip install --no-cache-dir poetry==1.2.0
RUN poetry self update
COPY pyproject.toml /usr/src/app
RUN poetry config virtualenvs.create false
RUN poetry install --no-root && rm -rf ~/.cache/pypoetry/{cache,artifacts}