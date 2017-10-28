
class ToDo:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item_value):
        new_items = []
        for element in range(0, len(self.items)):
            if self.items[element].get_value() != item_value:
                new_items.append(self.items[element])

        self.items = new_items

    def count(self):
        return len(self.items)
