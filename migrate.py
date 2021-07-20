from configparser import ConfigParser
from sql2nosql import Migrator

# Load the environment variables from the file
config = ConfigParser()
config.read("./docker-environment.env")

host = config["global"]["HOST"]

sql_config = {
    "host": host,
    "port": int(config["postgres"]["POSTGRES_EXPOSE"]),
    "username": config["postgres"]["POSTGRES_USER"],
    "password": config["postgres"]["POSTGRES_PASSWORD"],
    "database": config["postgres"]["POSTGRES_DATABASE"]
}

nosql_config = {
    "host": host,
    "port": int(config["mongo"]["MONGO_EXPOSE"]),
    "username": config["mongo"]["MONGO_USER"],
    "password": config["mongo"]["MONGO_PASSWORD"]
}

c = Migrator(
    sql_config=sql_config,
    nosql_config=nosql_config,
    sql_client="psycopg2",
    nosql_client="pymongo"
    )

c.migrate_data(tables=['"Album"'])
