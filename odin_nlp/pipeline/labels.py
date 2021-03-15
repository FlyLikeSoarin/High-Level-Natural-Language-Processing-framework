from .base import BasePipeline


class Feature(BasePipeline):
    def __init__(self, previous):
        super(self).__init__(previous)
        self.__config__ = {**self.__config__, type='feature'}


class Target(BasePipeline):
    def __init__(self, previous):
        super(self).__init__(previous)
        self.__config__ = {**self.__config__, type='target'}
