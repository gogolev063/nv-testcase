This application consists of 3 parts, each of which runs in its own docker container:
- REST API Web-service
- Client Application
- Database

## REST API Web-service

Implements the following endpoints:
- POST `/new`

    Сохраняет запись в базу данных и присваивает ей уникальный идентификатор uuid. Пример тела запроса:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

-  GET `/all`

    Отдаёт все добавленные записи, пример тела ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

- GET `/<uuid>`

    Отдаёт конкретную запись по запрошенному uuid. Если записи не существует, отдаёт HTTP 404. Пример успешного ответа:
    ```json
    {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"}
    ```

- GET `/<count>`

    Отдаёт запрошенное в <count> количество записей. Пример успешного ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

- DELETE `/<uuid>`

    Deletes an entry for the requested uuid from the database. If the record does not exist, it returns HTTP 404. If successful, it returns HTTP 200.

## Client Application

It runs together with the web service and constantly generates a random number (from 10 to 100) of random strings (letters, numbers, 16 characters) to insert into the database of the first API service.

At the same time, the application constantly requests 10 lines via the API and deletes them.

The number of deleted records is printed to the standard output stream every 10 seconds.

## Database

PostgreSQL is used as the database
