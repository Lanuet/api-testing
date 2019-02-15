from peewee import *


class DBConnection:

    def __init__(self, db_connection) -> None:
        super().__init__()
        self.host = db_connection["host"]
        self.dbname = db_connection["dbname"]
        self.username = db_connection["user"]
        self.password = db_connection["password"]
        self.port = db_connection["port"]
        self.engine = db_connection["engine"]
        self.conn = None

    def connect_to_db(self):
        print("Connectiong to database.....")
        conn = None
        if self.engine == "mysql":
            conn = MySQLDatabase(self.dbname,
                                 user=self.username,
                                 password=self.password,
                                 host=self.host,
                                 port=self.port)
        elif self.engine == "postgres":
            conn = PostgresqlDatabase(self.dbname,
                                      user=self.username,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port)
        self.conn = conn

    def get_rows(self, query):
        cursor = self.conn.execute_sql(query)
        return cursor.rowcount

    def get_data(self, query):
        data = self.conn.execute_sql(query)
        self.conn.close()
        return data.fetchall
