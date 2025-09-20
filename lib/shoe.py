#!/usr/bin/env python3

class Shoe:
    #pass
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  # use setter to validate input
        self.condition = "New"

    # getter for size
    def get_size(self):
        return self._size

    # setter for size with validation
    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    # property lets you use shoe.size directly
    size = property(get_size, set_size)

    # method that repairs the shoe
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
