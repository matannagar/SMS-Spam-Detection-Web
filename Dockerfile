FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./outputs /app/outputs
COPY ./static /app/static
COPY ./predict.py /app/predict.py
RUN pip install -r requirements.txt
COPY . /app

CMD [ "python" , "./app.py"]

