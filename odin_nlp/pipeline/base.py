class BasePipeline:

    args = None

    def __init__(self, *previous):
        self.__config__ = {}
        if self.args is None:
            self.previous = previous
        elif self.args == len(previous):
            self.previous = previous
        else:
            raise ValueError(
                f'{self.__name__} expects to get {self.args} argument(s)'
                f' but got {len(previous)}'
            )


    @classmethod
    def __lshift__(cls, *previous):
        return cls.__init__(*previous)

    # Identity placeholder in interface
    @staticmethod
    def transform(datum):
        return datum

    def get_data_iterator(self):

        data_iterator = zip(
            **[elem.get_data_iterator() for elem in self.previous]
        )
        for datum in data_iterator():
            yield self.transform(**datum)

    def get_data(self):
        return [list(get_data_iterator)]

    @property
    def config(self):
        previous_config = {}
        # Merge previous configs
        for elem in self.previous():
            for key, value in elem.config:
                if key in previous_config:
                    if previous_config[key] == value:
                        continue
                    if isinstance(previous_config[key], list):
                        if value in previous_config[key]:
                            continue
                        else:
                            previous_config.append(value)
                else:
                    previous_config[key] = value

        return {**previous_config,  **self.__config__}
