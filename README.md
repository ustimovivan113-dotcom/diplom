# Skydash Ad Board (SB1)

Дипломный проект по разработке бэкенда для сервиса объявлений.

## Стек технологий
- **Backend:** Python 3.11, Django 4.2, DRF
- **Database:** PostgreSQL
- **Auth:** JWT (SimpleJWT)
- **Docs:** Swagger (drf-spectacular)
- **Frontend:** React (Vite, Tailwind CSS, Lucide React)
- **Containerization:** Docker, Docker-compose

## Основной функционал
1. **Пользователи:** Регистрация, авторизация через Email, кастомная модель.
2. **Объявления:** Полный CRUD, фильтрация по цене, поиск по названию/описанию.
3. **Комментарии:** Система отзывов под объявлениями.
4. **Права доступа:** Просмотр доступен всем, редактирование — только авторам или админам.

## Запуск проекта

### С использованием Docker
1. Убедитесь, что у вас установлен Docker и Docker-compose.
2. Склонируйте репозиторий.
3. Выполните команду:
   ```bash
   docker-compose up --build
   ```
4. API будет доступно по адресу: `http://localhost:8000/api/`
5. Документация Swagger: `http://localhost:8000/api/docs/swagger/`

### Локальный запуск (без Docker)
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Выполните миграции:
   ```bash
   python manage.py migrate
   ```
3. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Тестирование
Для запуска тестов используйте pytest:
```bash
pytest
```
