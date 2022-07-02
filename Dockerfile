#FROM python:3
FROM --platform=linux/amd64 python:3


WORKDIR /sutom-solver

COPY requirements.txt /sutom-solver/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py"]

#EXPOSE 5000