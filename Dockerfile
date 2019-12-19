# 公式からpython3.8 on alpine linuxイメージをpull
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /usr/src

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# psycopg2のインストール
# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev \
#     && apk add postgresql-dev \
RUN pip install psycopg2-binary
#     && apk del build-deps

# Pipenvをインストール
RUN pip install --upgrade pip \
    && pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY Pipfile /usr/src/Pipfile
COPY Pipfile.lock /usr/src/Pipfile.lock

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --system --ignore-pipfile

# entrypoint.shをコピー
COPY entrypoint.sh /usr/src/entrypoint.sh

# ホストのカレントディレクトリ（現在はappディレクトリ）を作業ディレクトリにコピー
COPY . /usr/src/

# entrypoint.shを実行
ENTRYPOINT ["/usr/src/entrypoint.sh"]