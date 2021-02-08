# Trabeblog

This is a sample blog web application written in Python using the [Django web framework](https://www.djangoproject.com). 

## How to start the app

You must perform the following steps to start the app:

1. Install [poetry](https://python-poetry.org/):

```
$ pip install poetry
```

2. Create the [virtual environment](https://python-poetry.org/docs/managing-environments/) and install the project dependencies:

```
$ poetry install
```

3. Open a poetry shell and run the [migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/):

```
$ poetry shell
$ python manage.py migrate
```

4. Create an admin user:

```
$ python manage.py createsuperuser
```

5. Run the server:

```
$ python manage.py runserver
```
