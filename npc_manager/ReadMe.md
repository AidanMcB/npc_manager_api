### NPC Manager API

## Prerequisites
- Setup virtual environment and install requirements from requirements.txt file
`python -m venv venv`
`source venv/bin/activate` # venv\Scripts\activate on windows
`pip install -r requirements.txt`


## Running the Flask API
1. Manually set the variable `FLASK_APP` to the instance of your app
`export FLASK_APP=npc_manager`
2. Initialize the database (only necessary on first run)
`flask db init`
3. Create a migration script (SQL version of the model)
`flask db migrate`
4. Run the migration on your database
`flask db upgrade`
5. Run the Flask Server
`flask run`

### Make changes to the DB
1. Edit the model files in /app_name/models
2. Run a migration with a message describing what the change is
`flask db migrate -m "Remove column middle_name from User"`
3. Apply the migration to the db 
`flask db upgrade`
4. You can verify the update has worked by checking in the flash shell
`flask shell`
5. Then from within the shell, run:
```
from your_app_name import db
from your_app_name.models import User
db.inspect(User).c
```

### Running the Docker Container
To run this application locally, you will need to run two docker containers. One for postgresql and one for the flask API. The docker-compose.yml is set up to start both, assuming your env variables are set correctly.

1. Build the Docker image
`docker build -t npc-manager-api .`

2. Run Docker container
`docker run -d -p 5050:5000 npc-manager-api`

#### Troubleshooting Docker
- Try checking the docker logs with this command
`docker logs <container_id>`
- To get the container_id run
`docker ps`
- To stop a running docker container
`docker stop <container_id>`
- Build new docker container
`docker compose up --build`
- Check the running container is using the correct env variables
`docker exec -it <container_id> printenv | grep SQLALCHEMY_DATABASE_URI`
- To ensure the postgresql container is running, try connecting to it manually
`docker exec -it <db_container_id> psql -U <POSTGRES_USER> -d <POSTGRES_DB>`
- If tables are not available, run migrations inside a docker container (container must be running)
`docker compose exec web flask db upgrade`

