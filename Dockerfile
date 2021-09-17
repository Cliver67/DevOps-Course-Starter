FROM python:3.9-slim-bullseye as base

FROM base as stage-one

# stage-one specific stuff here

FROM base as stage-two
# stage-two specific stuff here

#set working directory
WORKDIR /app

#install Poetry
RUN pip install poetry

#copy the config files
COPY pyproject.toml poetry.toml poetry.lock ./

#install dependencies
RUN poetry install

#Copy project files
COPY . /app

#set startup and launch
#working port
EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0.:5000", "todo_app:create_app()"]


