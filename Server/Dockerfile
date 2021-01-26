FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk --update add bash nano

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["api.py"]
