# skglist.com

> Most voted places in Thessaloniki.


## Setup

The Django project is [`skglist`](/skglist). There is the [`main`](/main) Django app,
with all business logic.

Create virtualenv, enable it and then install requirements:
```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

> Note: This project uses [pip-tools](https://github.com/jazzband/pip-tools) for dependencies management.

You need to create a new file named `.env` in the root of this project once you cloned it.

`.env` should contain the following env variables:
```
DATABASE_URL="postgres://username:password@localhost:5432/db_name"
SECRET_KEY="thisisthesecretkey"
```


## Database

This project uses PostgreSQL. See above on how to configure it using the `.env` file.

> [How to: Create PostgreSQL DB](https://gist.github.com/sirodoht/0666e232e1baf76f76bac43eb2600e2b)

After creating your local database, you need to apply the migrations:
```sh
python manage.py migrate
```

Finally, you can run the Django development server:
```sh
python manage.py runserver
```

Or, run the production-grade `uwsgi` server:
```sh
uwsgi --ini=uwsgi.ini -H venv/
```

> Note: The `uwsgi` method does not read the `.env` file, so in this case you need to set the env vars in your shell.


## Colors

The 9 shades of blue. Light to dark.
```
#e7f5ff
#d0ebff
#a5d8ff
#74c0fc
#339af0
#228be6
#1c7ed6
#1864ab
```


## Code linting & formatting

```
black . && isort -y && flake8
```


## License

MIT
