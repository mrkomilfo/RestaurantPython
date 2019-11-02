import Models.Bill as Bill


class Order(dict):
    def __init__(self, id, time, bill):
        for key in bill.keys():
            self.setdefault(key, bill[key])
        self.id = id
        self.time = time
