from enum import Enum

from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase


class Database(Enum):
    SQLITE = 'Sqlite'
    POSTGRESQL = 'Postgresql'
    MYSQL = 'MySQL'


class Connector:

    def __init__(self, database, **kwargs):
        if database == Database.MYSQL:
            self.__init__mysql(**kwargs)
        if database == Database.POSTGRESQL:
            self.__init__postgresql(**kwargs)
        if database == Database.SQLITE:
            self.__init__sqlite(**kwargs)

    def __init__mysql(self, **kwargs):
        try:
            path = kwargs['database']
            self.database = MySQLDatabase(path, **kwargs)
        except KeyError:
            raise ValueError('Not enough arguments')

    def __init__postgresql(self, **kwargs):
        try:
            path = kwargs['database']
            self.database = PostgresqlDatabase(path, **kwargs)
        except KeyError:
            raise ValueError('Not enough arguments')

    def __init__sqlite(self, **kwargs):
        try:
            path = kwargs['database']
            self.database = SqliteDatabase(path, **kwargs)
        except KeyError:
            raise ValueError('Not enough arguments')

    def __enter__(self):
        self.database.connect()
        return self.database

    def __exit__(self):
        




# # SQLite database using WAL journal mode and 64MB cache.
# sqlite_db = SqliteDatabase('/path/to/app.db', pragmas={
#     'journal_mode': 'wal',
#     'cache_size': -1024 * 64})
#
# # Connect to a MySQL database on network.
# mysql_db = MySQLDatabase('my_app', user='app', password='db_password',
#                          host='10.1.0.8', port=3306)
#
# # Connect to a Postgres database.
# pg_db = PostgresqlDatabase('my_app', user='postgres', password='secret',
#                            host='10.1.0.9', port=5432)
