# URLShortener


Сервис для сокращения URL-ссылок с использованием FastAPI, PostgreSQL и Docker.

## Требования

* Python 3.13+
* pip
* Docker
* Docker Compose



## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/kantakt1234/URLShortener.git
cd URLShortener
```

Создайте файл .env и скопируйте в него содержимое файла .env.example. При необходимости измените переменные окружения

```bash
cp .env.example .env
```

Создайте базу данных

## Запуск с Docker Compose

Запустите приложение 

```bash
docker compose up
```

## Запуск без Docker Compose

Создайте базу данных

```bash
psql -U имя_пользователя -h хост -p порт
```

Выполните команду

```commandline
CREATE DATABASE имя_базы_данных;
```

Создайте виртуальное окружение

```bash
python3 -m venv .venv
```

Активируйте виртуальное окружение на macOS или Linux:

```bash
source .venv/bin/activate
```

На Windows: 

```powershell
.venv\Scripts\activate
```

Установите зависимости:

```bash
poetry install
```

Выполните миграции Alembic

```bash
alembic upgrade head
```

Запустите приложение:

```bash
uvicorn "app.main:app"
```

## Доступ к приложению


FastAPI http://127.0.0.1:8080/

Документация http://127.0.0.1:8080/docs
