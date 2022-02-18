import mysql.connector as mysql
from mysql.connector import Error
import sqlalchemy
from urllib.parse import quote_plus as urlquote
import matplotlib.pyplot as plt
import pandas as pd

# decouple is library for importing local variable for Linux OS
from decouple import config

class StudiKasus2:
    """
    Initiaze this class with some variable like host, port and user
    to connect to the database.
    """
    def _init_(self, host, port, user, password):
        self.host = 'localhost' #Fill with your host name
        self.port = '3306' #Fill with your port number
        self.user = 'root' #Fill with your user name
        self.password = config('PASSDB') #Fill with your password or local variable name

    def check_conn(self):
        self.conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )

    """
    mysql.connect is the built-in function to try connect to the DB
    with the host, port, user, and password parameter from def _init_
    """
    def connect_db(self):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                print("Database connected!")
                # If the connection is successfull will print "Database Connected"
        except Error as e:
            # If can't connect to the database, it will print this error message
            print("Error while connecting to MySQL", e)
    
    """
    Function to ceate database,
    db_name is the parameter you can input in it and will be
    the name of your database.
    """
    def create_db(self, db_name):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                cursor.execute("CREATE DATABASE {}".format(db_name))
                print('Database ', db_name, ' created!')
        except Error as e:
            print("Error while connecting to MySQL", e)

    """
    Function to ceate table,
    db_name and table_name is the parameter you can input in it and will be
    the name of your database.
    """
    def create_table(self, db_name, table_name, df):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                cursor.execute("USE {}".format(db_name))
                cursor.execute("CREATE TABLE {}".format(table_name))
        except Error as e:
            print("Error while connecting to MySQL", e)

        engine_stmt = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (self.user, urlquote(self.password),
                                                            self.host, self.port, db_name)
        engine = sqlalchemy.create_engine(engine_stmt)

        df.to_sql(name=table_name, con=engine,
                  if_exists='append', index=False, chunksize=1000)

    
    # NOT REVISED YET
    def load_data(self, db_name, table_name):
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM {}.{}".format(db_name, table_name))
                result = cursor.fetchall()
                return result
        except Error as e:
            print("Error while connecting to MySQL", e)

    def import_csv(self, path):
        return pd.read_csv(path, index_col=False, delimiter=',')
