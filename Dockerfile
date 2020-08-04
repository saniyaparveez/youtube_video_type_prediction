FROM python:3.6
MAINTAINER Saniya Parveez
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
