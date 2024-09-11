# Проект «Project_Brendwall»
# Описание
Тестовое задание.
На этом сайте можно создать продукт и добавить его в общую таблицу продуктов.

Проект доступен только на локалхосте http://127.0.0.1:8000/
URL:
admin/ - админка
api/products/ - апишка продуктов (GET запрос)
api/create-product/ - апишка на создание (POST запрос)
add-product/ - создать продукт через html страницу

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/goldenlion52rus/Test_Brendwall
cd Test_Brendwall
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Над проектом работал: 
https://github.com/goldenlion52rus