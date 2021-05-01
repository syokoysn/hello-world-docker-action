# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-slim-buster

# 作業ディレクトリを設定
WORKDIR /usr/src/

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    wget \
    git \
    gnupg2

#install google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \ 
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update -y && apt-get install -y google-chrome-stable

# Pipenvをインストール
RUN pip install --upgrade pip \
    && pip install pipenv \
    pip install chromedriver-binary~=$(/usr/bin/google-chrome --version | perl -pe 's/([^0-9]+)([0-9]+\.[0-9]+).+/$2/g') 

RUN  pip install \
    pandas \
    selenium \
    beautifulsoup4 \
    boto3 \
    sqlalchemy \
    autopep8 \
    flake8 \
    black
