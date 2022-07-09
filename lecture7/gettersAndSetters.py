class Backpack:

    def __init__(self):
        self._item = []

    def get_items(self):
        return self._item

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._item = new_items
        else:
            print("Please enter a valid list of items")


my_bagpack = Backpack()
print(my_bagpack.get_items())
my_bagpack.set_items(['water bottles', 'sleeping bags', 'Firstaid'])

print(my_bagpack.get_items())
