FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY diary /app/diary/
COPY entries /app/entries/
COPY *.py /app/

RUN ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:9595"]