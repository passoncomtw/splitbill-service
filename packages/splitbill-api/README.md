# Split bill API

## Dev On Local

### Install Package

```sh
pip install -r requirements.txt
```

### Create .env file at root dir

```.env
DEBUG=True | False
SQLALCHEMY_ECHO=True | False //print sql log
DB_URL=user:password@url
DB_NAME=db-name
```

### Start Server

```sh
flask run
```

or

```sh
# hotload mod
flask --debug run
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
