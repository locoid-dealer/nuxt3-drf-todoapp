FROM python:3.11.3-buster

WORKDIR /app

ENV PYTHONPATH /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
&& pip install poetry

RUN poetry config virtualenvs.create false

COPY src/pyproject.toml pyproject.toml
RUN poetry install

CMD ["bash"]