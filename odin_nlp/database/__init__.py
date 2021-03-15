import os

from .schema import load_schema


class Database:
    def __init__(self):
        self.schema = load_schema()
        self.queryset = None

        self.models = {
            model.__name__: model
            for model in self.schema.BaseModel.__subclasses__()
        }

    def get_model(self, name):
        return self.models[name].select()

    def use(self, queryset):
        self.queryset = queryset

    def get_q
