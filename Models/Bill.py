class Bill(dict):
    def add(self, section):
        self.setdefault(section.name, section)

    def remove(self, key):
        self.pop(key)
