FROM python:3.7

RUN apt-get update

COPY requirements.txt . 

WORKDIR /python-docker

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]