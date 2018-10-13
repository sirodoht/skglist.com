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

From [Open color](https://yeun.github.io/open-color/).

The 9 shades of blue, for places. Light to dark.
```
1: #e7f5ff
2: #d0ebff
3: #a5d8ff
4: #74c0fc
5: #4dabf7
6: #339af0
7: #228be6
8: #1c7ed6
9: #1971c2
```

The 9 shades of red, for lists. Light to dark.
```
1: #fff5f5
2: #ffe3e3
3: #ffc9c9
4: #ffa8a8
5: #ff8787
6: #ff6b6b
7: #fa5252
8: #f03e3e
9: #e03131
```


## Code linting & formatting

```
black . && isort -y && flake8
```


## License

MIT
