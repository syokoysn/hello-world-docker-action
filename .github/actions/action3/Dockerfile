# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-slim-buster
# 作業ディレクトリを設定

WORKDIR /github/workspace/

RUN pwd
COPY check.py /check.py
RUN pwd
RUN ls
RUN export PYTHONPATH="/github/workspace:$PYTHONPATH"
CMD ["python", "/check.py"]