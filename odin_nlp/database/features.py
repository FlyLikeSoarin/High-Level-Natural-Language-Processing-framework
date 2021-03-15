class FeatureMapper:

    def __init__(self, model, fields=[]):
        for field in fields:
            if type(field):
                pass
