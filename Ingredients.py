class Ingredients():
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def opprinter(self):
        print(self.name)
        print(self.quantity)
        print(self.unit)
