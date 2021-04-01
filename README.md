# Cultural Part of Scholarship Application
Back-end для заполнения студентом форм о достижениях в культурно-творческой деятельности. Используется Python, FastAPI, PostgreSQL, Heroku.

[Ссылка на Heroku](https://culturalpart.herokuapp.com/items)

## How to launch
### Installing dependencies
    pip install -r requirements.txt
### Running application (local server)
	uvicorn app.main:app --reload

## Функционал со стороны заполняющего (возможный минимум)

- заполнить заявку
- посмотреть статус заявки
- прикрепить документы, подтверждающие достижения

## Функционал со стороны проверяющего
- изменить статус заявки (принято/отклонено)
- вернуть заявку на исправление, необходмые для исправления ошибки будут выделены

