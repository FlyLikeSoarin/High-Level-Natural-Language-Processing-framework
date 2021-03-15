from typing import Iterable

from .base import BasePipeline


class FromDB(BasePipeline):
    sep = '.'

    def __init__(self, path):
        # Path as string
        if isinstance(path, str):
            if len(path.split(self.sep)) != 2:
                raise ValueError('Path should be format as "Model.Field"')
            self.model, self.field = path.split(self.sep)
        # Path as list or tuple
        elif isinstance(path, (tuple, list)):
            if len(path) != 2:
                format_help = (
                    '["Model", "Field"]' if isinstance(path, list) else '("Model", "Field")'
                )
                raise ValueError(f'Path should be format as {format_help}')
            self.model, self.field = path
        else:
            raise ValueError('Path format is not supported')

        self.__config__ = {
            'model': self.model,
            'field': self.field,
        }

    def get_data_iterator(self):
        table = DATABASE.get_table()
        filed = DATABASE.resolve_name(self.model, self.field)
        for row in table:
            yield row[field]

    def get_data(self):
        return list(self.get_data_iterator())

    @property
    def config(self):
        return self.__config__
