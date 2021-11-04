FROM python:3.9-slim-bullseye as base

#Common needs
#Set Working Directory
WORKDIR /todo_app
#install Poetry
RUN pip install poetry
#copy the config files
COPY pyproject.toml poetry.toml poetry.lock ./
#install dependencies
RUN poetry install
#Copy project files
COPY . ./
#set startup and launch
#working port
EXPOSE 5000

FROM base as Development


# Development Specific needs here
CMD ["poetry", "run", "flask", "run", "--host",  "0.0.0.0"]    


FROM base as Production
# Production Specific needs here
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0.:5000", "todo_app.app:create_app()"]


