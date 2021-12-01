FROM python:3.9 as base

WORKDIR app/

COPY . .

RUN pip install --upgrade pip

RUN pip install 'poetry==1.0.0'

RUN apt update
RUN apt install postgresql -y

RUN poetry install

FROM base as tests

RUN ["poetry", "run", "pytest"]

FROM base as development

ENTRYPOINT ["poetry", "run", "python"]

CMD ["shipay/wsgi.py"]
