class Staff(dict):
    def recruit(self, identity, employee):
        self.setdefault(identity, employee)

    def dismiss(self, identity):
        self.pop(identity)
