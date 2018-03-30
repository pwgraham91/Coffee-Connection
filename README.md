# Coffee Connection
App to help coworkers build connections across departments

## Set Up

### Install requirements

### Make virtual environment
`virtualenv -p python3 venv`

### Source into virtual environment
`source venv/bin/activate`

#### Install Python Requirements
`pip install -r requirements`

#### Install Javascript Requirements
`yarn` (will install in /app/static/node_modules)
`cd app/static/js/react && yarn`
`npx build-react-dev`

#### Build React

### Setup database
Make sure your local database is running and open it with
`psql postgres`

Create a new database with `CREATE DATABASE coffee_connection`

`python db_create.py`

`python db_migrate.py`

### Create config
In the root directory, make a file called config.py using example_config.py as a template then replace all of the keys with your own

## Run the app
`python run.py`
