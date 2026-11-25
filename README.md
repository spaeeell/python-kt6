
# КТ №6 — Контейнеризация и автоматический деплой

## Описание
FastAPI-приложение с JWT-авторизацией, PostgreSQL, Redis, Celery и GraphQL.

## Реализовано
- Dockerfile для FastAPI
- Docker Compose с PostgreSQL, Redis и Celery
- Подключение к базе данных через переменные окружения
- Автоматические тесты pytest через GitHub Actions
- Публичный деплой FastAPI на Railway

## Публичный адрес

Swagger UI:
https://python-kt6-production-37f1431b.up.railway.app/docs

## Локальный запуск

Для запуска необходим Docker и локальный файл .env.docker с настройками подключения.

docker compose --env-file .env.docker up --build

## Тестирование

python -m pytest -v
