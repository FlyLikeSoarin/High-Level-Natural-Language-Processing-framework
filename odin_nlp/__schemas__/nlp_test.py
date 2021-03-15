from peewee import *

database = PostgresqlDatabase('nlp_test', **{'host': '127.0.0.1', 'port': 5432, 'user': 'nlp_test', 'password': 'wardZ1807'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Migratehistory(BaseModel):
    migrated = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'migratehistory'

class Sales(BaseModel):
    client = CharField()
    datetime = DateTimeField()
    description = CharField()
    price = IntegerField()

    class Meta:
        table_name = 'sales'

