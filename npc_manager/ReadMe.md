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
````
from your_app_name import db
from your_app_name.models import User
db.inspect(User).c
```
