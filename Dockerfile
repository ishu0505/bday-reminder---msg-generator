# Dockerfile, Image, Container

FROM python:3.9
ADD mail.py .
ADD Birthdays.csv .
ADD traverseBdaycsv.py .
ADD main.py .
RUN pip install  mime



RUN ["python", "./main.py"]
