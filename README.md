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

Создайте файл .env и скопируйте в него содержимое файла .env.example


```bash
cp .env.example .env
```
## Запуск с Docker Compose



Запустите приложение 

```bash
docker compose up
```

## Запуск без Docker Compose

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

Запустите приложение:

```bash
uvicorn "app.main:app"
```
