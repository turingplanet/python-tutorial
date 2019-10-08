class MyDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def put(self, key, value):
        self[key] = value

    def get(self, key):
        return self[key]