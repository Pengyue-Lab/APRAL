"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader


app = Flask(__name__)
def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )

    return pool



db = init_connection_engine()

# fullname = 'Atari 2600_'
# initial = '2600_'
# conn = db.connect()
# query = 'Update Platform set FullName = "{}" where Initial = "{}";'.format(fullname, initial)
# conn.execute(query)
# conn.close()


# conn = db.connect()
# query = 'Insert into Game values("{}",{},"{}","{}",{},{},{},{},{},{},"{}","{}")'.format('A',1234,'Action','Acquire',1,2,3,4,5,6,'1-Up Studio','E10+')
# conn.execute(query)
# conn.close()



# conn = db.connect()
# userId = 'Alia39'
# query = 'Delete from User where UserId = "{}";'.format(userId)
# conn.execute(query)
# conn.close()

# conn = db.connect()
# query_results = conn.execute("(Select DevName as Name,count(*) as Num From Game natural join Play natural join User where Gender = 'FeMale' Group by DevName order by Num desc limit 8)union(Select PubName as Name,count(*) as Num From Game natural join Play natural join User where Gender = 'FeMale' Group by PubName order by Num desc limit 7)").fetchall()
# conn.close()
# print(query_results)


# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
# from app import routes
