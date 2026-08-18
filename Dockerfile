FROM python:3.13.15-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /project

RUN pip install --upgrade pip wheel "poetry==2.4.1"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY app /project/app

copy alembic.ini .

RUN chmod +x /project/app/prestart.sh

ENTRYPOINT ["/project/app/prestart.sh"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]