## Проект "Friday-WSGI-Framework"

### Базовая документация к проекту

Основные системные требования:

* Python 3.11
* Jinja2 3.1.2
* Зависимости (Python) из requirements.txt

Разработка фреймворка в помощи создания сайтов. 

### Установка необходимого ПО

#### Обновляем информацию о репозиториях

```
apt update
```

#### Установка virtualenv

virtualenv

```
apt install python3-venv
```

#### Настраиваем виртуальное окружение

При необходимости, для установки менеджера пакетов pip выполняем команду:

```
apt install python3-pip
```

Клонируем проект с GitHub:

```
git clone https://github.com/EvgenPalimov/friday_framework.git
```

Создаем и активируем виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Ставим зависимости:

```
pip3 install -r requirements.txt
```

Запускаем временный сервер:

```
python run.py
```


### После этого в браузере можно ввести http://127.0.0.1:8000/ и откроется проект.
