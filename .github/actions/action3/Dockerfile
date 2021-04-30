# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-slim-buster
# 作業ディレクトリを設定
WORKDIR /usr/src/

COPY check.py /usr/src/check.py
COPY /mypackage /usr/src/mypackage 
CMD ["python", "/usr/src/check.py"]