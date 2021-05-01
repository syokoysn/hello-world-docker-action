# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-slim-buster
# 作業ディレクトリを設定

WORKDIR /github/workspace/

RUN pwd
COPY check.py /github/workspace/check.py
RUN pwd
RUN ls
CMD ["python", "/github/workspace/check.py"]