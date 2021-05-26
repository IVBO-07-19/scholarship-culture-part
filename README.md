# Cultural Part of Scholarship Application
Back-end для заполнения студентом форм о достижениях в культурно-творческой деятельности. Используется Python, FastAPI, PostgreSQL, Heroku.

[![Python application](https://github.com/IVBO-07-19/scholarship-culture-part/actions/workflows/tests.yml/badge.svg)](https://github.com/IVBO-07-19/scholarship-culture-part/actions/workflows/tests.yml)

## Heroku
 ***[Ссылка на главную страницу](https://culturalpart.herokuapp.com/docs)***
 
**Для регистрации пользователя: PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI**

### Ссылки на определенные пункты из приложения №4 
#### (Достижения студента в культурно-творческой деятельности)
1. [Получение награды (приза) за результаты культурно-творческой деятельности, осуществленной в рамках деятельности, проводимой Университетом или
иной организацией, в том числе в рамках конкурса, смотра и иного аналогичного международного, всероссийского, ведомственного,
регионального мероприятия](https://culturalpart.herokuapp.com/api/culture/prizes/)
   ![image](https://sun9-25.userapi.com/impf/WJgQSEh1_pMKSmY3ltOth9NZr8xE3g65UdCebg/gHuruxK8eQw.jpg?size=668x392&quality=96&sign=ef439b6cf046ea53cd54930cca33b79c&type=album)
   
   
2. [Публичное представление созданного произведения литературы или искусства](https://culturalpart.herokuapp.com/api/culture/artworks/)
   ![image](https://sun9-9.userapi.com/impf/SGK-fnP8oaiUHkHGUiXFiNtt_jpxnxdjTFe8dg/Y1EDcwMeoRg.jpg?size=703x374&quality=96&sign=b99b67c555fbd2e737a9b8d2d7f73508&type=album)
  
 
3. [Систематическое участие в проведении (обеспечении проведения) публичной культурно-творческой деятельности воспитательного, пропагандистского
характера и иной общественно значимой публичной культурно-творческой деятельности](https://culturalpart.herokuapp.com/api/culture/activity/)
   ![image](https://sun9-31.userapi.com/impf/QYhy7u_1qZHGC3r0HSCWns6GGDVkBFHKb1zbUQ/ejrAJ4-_Ksg.jpg?size=691x375&quality=96&sign=442b5ee4e73de00981de560fa8bf5d8b&type=album)
   
   Участие в составе творческого коллектива Университета или отдельно будет осуществляться в одной таблице (булевое значение: 0 - не в составе, 1 - в составе)

## How to launch
### Creating virtual environment
    python3 -m venv venv
 Activate a script in the virtual environment which named Activate.ps1 or Activate.bat
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

