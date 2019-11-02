class Bill(dict):
    def add(self, section):
        if section.name in self.keys():
            self[section.name].increment()
        else:
            self.setdefault(section.name, section)

    def remove(self, key):
        if self[key].number > 1:
            self[key].decrement()
        elif self[key].number == 1:
            self.pop(key)

    def getCost(self):
        total = 0
        for section in self.values():
            total += section.get_cost()
        return total
