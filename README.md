# Проект API для мобильного приложения

1. **Установите Python и зависимости**:
   ```bash
   pip install -r requirements.txt

2. **Поменяйте настройки для подключения к БД (PostgreSQL) в main_app/settings.py
3. Выполните миграции
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. Загрузите тестовые данные для моделей:
    ```bash
      python manage.py loaddata initial_data.json
5. Запустите сервер
    ```bash
      python manage.py runserver

6. Проверить API можно в файле test.py (или же в Postman)