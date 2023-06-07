# Тестовый проект
Проект сделан с использованием Fastapi, для разработки api университета.
Проект содержит следующие каталоги и файлы

Файлы:
1. main.py: Точка входа проекта
2. database.py: Единая точка подключения к базе postgresql c использованием asyncpg
3. README.md: Описание проекта
4. requirements.txt: Зависимости

Каталоги:
1. task1and2: включает в себя 2 sql скрипта для решения первого и второго задания, 
    а также схема БД спроектированная при помощи draw.io
2. config: хранит чувствительные данные
3. courses, grades, students, teachers: хранят в себе файлы models.py, router.py, schemas.py

## Установка и запуск
1. Склонируйте репозиторий на свой компьютер:
   ```bash
    git clone https://github.com/kha1l/university.git
2. Перейдите в каталог проекта:
   ```bash
    cd university
3. Создайте виртуальное окружение и активируйте его:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
4. Установите зависимости проекта:
   ```bash
    pip install -r requirements.txt
5. Установите PostgreSQL с помощью следующей команды:
   ```bash
   sudo apt update
   sudo apt install postgresql postgresql-contrib
6. Откройте интерактивную оболочку psql
   ```bash
   sudo -u postgres psql
7. В интерактивной оболочке psql создайте базу данных "university" с помощью следующей команды
   ```bash
   CREATE DATABASE university;
8. Создайте нового пользователя "postgres" с паролем "postgres" и предоставьте ему полные права 
доступа к базе данных "university"
   ```bash
   ALTER USER postgres WITH PASSWORD 'postgres';
   GRANT ALL PRIVILEGES ON DATABASE university TO postgres;
9. Запустите sql-скрипт
   ```bash
   psql -U postgres -d university -f home/{your_name}/university/task1and2/task1.sql>;
10. Запустите веб-приложение:
    ```bash
    uvicorn main:app --reload
11. Откройте браузер и перейдите по адресу [http://localhost:8000/docs](http://localhost:8000/docs) для 
просмотра документации приложения на Swagger.

Для Windows скачать PostgresQL с официального сайта, с ним вместе идет pgAdmin4, все операции по 
созданию БД university можно проделать там. Так же там можно проверить работу скрипта sql из второй части задания.

На Ubuntu запуск идентичен task1 или запустить при помощи какого либо инструмента для работы с БД, например Dbeaver, 
Pycharm Professional.
   
   `psql -U postgres -d university -f home/{your_name}/university/task1and2/task2.sql>;`


## API

Проект предоставляет следующие API-эндпоинты:

- `POST /students`: Cоздать нового студента.
- `GET /students/{student_id}`: Получить информацию о студенте по его id.
- `PUT /students/{student_id}`: Обновить информацию о студенте по его id.
- `DELETE /students/{student_id}`: Удалить студента по его id.
- `GET /teachers`: Получить список всех преподавателей.
- `POST /courses`: Создать новый курс.
- `GET /courses/{course_id}`: Получить информацию о курсе по его id.
- `GET /courses/{course_id}/students`: Получить список всех студентов на курсе.
- `POST /grades`: Создать новую оценку для студента по курсу.
- `PUT /grades/{grade_id}`: Обновить оценку студента по курсу.