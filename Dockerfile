FROM python:latest
COPY code /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]