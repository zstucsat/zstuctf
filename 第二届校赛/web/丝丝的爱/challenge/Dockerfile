FROM python:3.6
WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
COPY gunicorn.conf.py ./gunicorn.conf.py
COPY flag.txt /fl4g

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 80

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]