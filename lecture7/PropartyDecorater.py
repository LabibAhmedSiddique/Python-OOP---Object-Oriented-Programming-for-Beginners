class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("calling the getters")
        return self._items

    @items.setter
    def items(self, new_items):
        print("calling the setters")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("enter list")


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = ["bottle", "first-aid", "walet"]
print(my_backpack.items)
