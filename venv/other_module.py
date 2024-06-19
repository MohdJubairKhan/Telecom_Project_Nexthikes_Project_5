from sqlalchemy import create_engine
import pandas as pd
"""
a function that connect to the local database
"""
def create_conn():
    engine = None
    try:
        # Create an engine that connects to PostgreSQL server
        db_username = 'root'
        db_password = 'root'
        db_host = 'localhost'
        db_port = 3306
        db_name = 'telecome_project'

        engine = create_engine(f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
        print("Connection successful")
    except Exception as error:
        print(error)

    return engine

"""
a function that that accept engine, and table_name as an argument and return pandas data fream
"""
def fetch_data(engine, user_data):
    df = None
    try:
        # Execute a query and fetch all the rows into a DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {user_data};", engine)
    except Exception as error:
        print(error)

    return df
