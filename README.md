# hillel_django_students_tracker
Studying django students tracker.

This project supposed to run on `python3`


## Location
This site locate [GitHub Pages](https://github.com/miha-pavel/hillel_students_tracker)


## Before first launch
```
1. python3 -m venv env
2. . env/bin/activate
3. pip install -r requirements.txt
4. Configure project using `local_setings.dev.py` as example. Your local settings should be written in `local_setings.py`
5. python manage.py migrate
```


## Run Django project
```
python manage.py runserver
```
Or use makefile guide


## Makefile guide
* ```make run``` - will run Django developer server at 8000 port
* ```make test``` - will test the project with --keepdb option
* ```make pep8``` - will check the code with pylint
* ```make sh_p``` - will run django shell_plus
* ```make migrate``` - will run django "./manage.py migrate" command


### Домашнее задание 4
Добавлено: 29.12.2019 14:33

Реализовать функионал
1. [x] Создать вью функцию которая будет генерировать одного студенты с случайными параметрами.
2. [x] Написать команду которая будет генерировать 100 случайных студентов (python manage.py generate_students) (https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
3. [x] Cоздать модель Group добавить несколько полей (название и тип по-желанию)


### Домашнее задание 5
Добавлено: 05.01.2020 14:41

Реализовать функционал
1. [x] Перенести весь функционал студентов на новую модель Teacher. В результате должен быть фильтр по полям first_name last_name email с оператором OR (sql) (8 баллов)
2. [x] Добавить функционал студентов на модель Group (2 балла)


### Домашнее задание 6
Добавлено: 09.01.2020 21:26

Добавить формы. 
Решение прислать в виде Пул реквеста.

1. [x] Создать форму добавления для Учителя
2. [x] Создать форму добавления группы.

### Домашнее задание 7
Добавлено: 12.01.2020 16:42

Реализовать функионал
Для учителей и групп должно быть

1. [x] Возможность редактировать запись в базе данных
2. [x] Для работы с urls во вьюхах и шаблонах использовать reverse и {% url 'name' %}
3. [x] Создать в приложении учителя файл urls.py вынести все урлы связанные с этим приложением и заинклюдить их в основном файле utls.py
4. [x] Добавить логгирование на отправку почты (записывать почту, сабджект в текстовый файл)
5. [x] Каждые элемент в списке (студент, группа, учитель) должен быть кликабельным и вести на страницу редактирования соответствующего объекта.
        Добавить в шаблонах кнопку которая будет вести на добавление объекта.