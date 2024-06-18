ORMParser is an application for creating a database system based on the configuration settings of a json file.



How to work with ORMParser.



Step 1. Clone a remote repository.
```sh
git clone https://github.com/DuoRoudenL/ORMParser.git
cd ORMParser
```

Step 2. Install and configure PostgreSQL.

Step 3. Download and install Docker Desktop or Docker Toolbox.

Step 4. Open the .env file and set your own values.
```sh
POSTGRES_USER=your_user_name
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database

DATABASE_HOST=your_gost
DATABASE_PORT=your_port
DATABASE_NAME=your_database
DATABASE_USER=your_user_name
DATABASE_PASSWORD=your_password
```

Step 5. Open the file table_definition.json and set your own database configuration.
```sh
{
    "tables": [
        {
            "name": "users",
            "columns": [
                {
                    "name": "id",
                    "type": "integer",
                    "primary_key": true
                },
                {
                    "name": "username",
                    "type": "varchar"
                },
                {
                    "name": "email",
                    "type": "varchar"
                },
                {
                    "name": "created_at",
                    "type": "timestamp"
                }
            ]
        },
        {
            "name": "posts",
            "columns": [
                {
                    "name": "id",
                    "type": "integer",
                    "primary_key": true
                },
                {
                    "name": "title",
                    "type": "varchar"
                },
                {
                    "name": "content",
                    "type": "text"
                },
                {
                    "name": "user_id",
                    "type": "integer",
                    "foreign_key": {
                        "table": "users",
                        "column": "id"
                    }
                },
                {
                    "name": "created_at",
                    "type": "timestamp"
                }
            ]
        },
        {
            "name": "comments",
            "columns": [
                {
                    "name": "id",
                    "type": "integer",
                    "primary_key": true
                },
                {
                    "name": "post_id",
                    "type": "integer",
                    "foreign_key": {
                        "table": "posts",
                        "column": "id"
                    }
                },
                {
                    "name": "content",
                    "type": "text"
                },
                {
                    "name": "user_id",
                    "type": "integer",
                    "foreign_key": {
                        "table": "users",
                        "column": "id"
                    }
                },
                {
                    "name": "created_at",
                    "type": "timestamp"
                }
            ]
        }
    ]
}
```

Step 6. Open Docker Command Console:
```sh
cd ORMParser
docker-compose build
docker-compose up -d
```

Step 7. Start the container and create the database according to the previously specified configuration.
```sh
docker-compose run main table_definition.json
```

Step 8. View the list of created tables.
```sh
docker exec -it postgres_db psql -U your_user_name your_database
\dt
```

Step 9. Stop containers and exit command console.
```sh
docker-compose down
exit
```