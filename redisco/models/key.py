class Key(str):
    def __getitem__(self, key):
        return Key(u"%s:%s" % (self, key))
