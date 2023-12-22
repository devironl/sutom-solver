#FROM python:3
FROM python:latest


WORKDIR /sutom-solver

COPY requirements.txt /sutom-solver/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py"]

#EXPOSE 5000