# Split bill API

## Dev On Local

### Install Package

```sh
pip install -r requirements.txt
```

### Make sure .env

```
DEBUG=True | False
SQLALCHEMY_ECHO=True | False
DB_URL=user:password@url
DB_NAME=db-name
```

### Start Server

```sh
flask run
```

### Swagger API Path

```
http://127.0.0.1:5000/doc
```

## Testing

```sh
pytest
```


## DB

### Init DB
```sh
flask db upgrade
```

### Seed mock data for DB
```sh
flask seed
```
