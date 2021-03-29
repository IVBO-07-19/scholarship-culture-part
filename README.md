# Cultural Part of Scholarship
Back-end для заполнения студентом форм о достижениях в культурно-творческой деятельности. Используется Python, FastAPI, PostgreSQL, Heroku.

[Ссылка на Heroku](https://culturalpart.herokuapp.com/api/cultural-part/example)

## How to launch
### Installing dependencies
    pip install -r requirements.txt
### Running application (local server)
	uvicorn app.main:app --reload


## Разработка
На всех этапах мы будем работать с тремя группами:
- Группы №1 и №2 общаются с внешним миром
- Группа №3 с внутренним (университетским)

_Этап 0. Подготовка Базы Данных._
Здесь надо будет проанализировать и понять как мы будем заносить и обновлять информацию о культурно-творческих мероприятиях по 3 направлениям:
1. Награды за культурно-творческую деятельность
2. Публичное представление произведения литературы или искусства
3. Участие в культурно-творческих мероприятиях университета

_Этап 1. Создание актуальной Формы._
Соискатель отправляет запрос через ЛК на заполнение 4-ого Приложения (культура).
Сервер получает запрос -> Проверяет актуальность БД -> Обновляет при необходимости -> Создает форму:
- Группа 1: наполняет menubar с выбором мероприятия
- Группа 2: наполняет menubar с выбором места публичного представления
- Группа 3: наполняет menubar с выбором мероприятия

_Этап 2. Получение актуальной формы и её заполнение соискателем._
Соискатель выбирает из menubar свой вариант (если его нет, предусмотреть "Иное", для ручного ввода) и для:
- Группа 1: при выборе своего варианта, все поля, кроме Баллов и Места (Призер, Победитель, 1,2,3 ???), заполняются автоматически (в соответствии с информацией о мероприятии из БД)
- Группа 2: вручную вводит название созданного произведения (надо будет понять, как стандартизировать)
- Группа 3: вручную заполняет "Выполненные работы по мероприятию"; Подтверждащий должен автоматически определятся на Этапе 0.

_Этап 3. Получение и обработка заполненного Приложения на сервер._
Форма разбивается на 2 Блока:
- Первый включает Группы №1 и №2. 
- Второй включает Группу №3.

В Блоке №1 происходит проверка соответствия введенных данных (как проверять участие пока не понятно).
Во Блоке №2 идет рассылка по внутренней почте университета Ответственным за подтверждение участия соответсвующих заявок (лучше, чтобы они волнами собирались в блоки и уже списками отправлялись).

## Примерное описание работы
Пользователь с помощью полей для ввода заполняет информацию о своих достижениях: название мероприятия, его уровень и дата проведения, а также степень участия студента. Некоторые поля, как уровень мероприятия и степень участия, можно заполнить, выбрав необходимый вариант из предложенных, а остальные пользователь заполняет самостоятельно. Также студент прикладывает в специальном поле копии документов, подтверждающих введённую раннее информацию. Это поле является обязательным, без его заполнения заявка не будет рассмотрена. Также при отправке введённых данных производится их проверка, то есть студент не может отправить пустые ячейки без какой-либо информации. 

## Функционал со стороны заполняющего (возможный минимум)

- заполнить заявку
- посмотреть статус заявки
- прикрепить документы, подтверждающие достижения

## Функционал со стороны проверяющего
- изменить статус заявки (принято/отклонено)
- вернуть заявку на исправление, необходмые для исправления ошибки будут выделены

