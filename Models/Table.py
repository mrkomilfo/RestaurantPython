class Table(dict):
    def upd(self, items_list):
        for first in items_list:
            for second in items_list:
                if first is not second:
                    self[first][second] += 1

    def add(self, name):
        if name not in self.keys():
            self.setdefault(name, dict())
            for existed_name in self.keys():
                self[existed_name].setdefault(name, 0)
                self[name].setdefault(existed_name, 0)

    def delete(self, name):
        self.pop(name)
        for item in self.keys():
            self[item].pop(name)
