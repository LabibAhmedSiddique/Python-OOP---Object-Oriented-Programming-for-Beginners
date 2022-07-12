class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("add valid item")

    def remove_items(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print("items aren't in the backpack")

    def has_items(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)

    def add_multiple_items(self, items):
        for item in items:
            self.add_items(item)


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_items("water bottle")
print(my_backpack.items)
my_backpack.add_items("sleeping bag")
print(my_backpack.items)
has_water = my_backpack.has_items("water bottle")
print(has_water)
my_backpack.remove_items("water bottle")
print(my_backpack.items)
my_backpack.add_items("water bottle")
my_backpack.add_items("candy")
my_backpack.show_items()
my_backpack.show_items(True)
my_backpack.add_multiple_items(["chargers, torch"])
print(my_backpack.items)
