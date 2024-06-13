#FROM ubuntu:latest
#LABEL authors="cyxov"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.12-slim
LABEL authors="cyxov"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "MainFolder/test.py"]