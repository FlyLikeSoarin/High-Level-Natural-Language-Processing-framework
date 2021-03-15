from peewee import *

database = PostgresqlDatabase('nlp_test', **{'user': 'nlp_test'}, autocommit=True)

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
