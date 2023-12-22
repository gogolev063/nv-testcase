This application consists of 3 parts, each of which runs in its own docker container:
- REST API Web-service
- Client Application
- Database

## REST API Web-service

Implements the following endpoints:
- POST `/new`

    Saves an entry to the database and assigns it a unique uuid. Example of the request body:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

-  GET `/all`

    Returns all the added entries, an example of the response body:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

- GET `/<uuid>`

    Returns a specific record by the requested uuid. If the record does not exist, it returns HTTP 404. Example of a successful response:
    ```json
    {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"}
    ```

- GET `/<count>`

    Returns the number of records requested in <count>. Example of a successful response:
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
