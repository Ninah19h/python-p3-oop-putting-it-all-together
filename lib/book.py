#!/usr/bin/env python3

class Book:
    #pass
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count  # go through setter for validation

    # getter for page_count
    def get_page_count(self):
        return self._page_count

    # setter for page_count with validation
    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    # property so you can use book.page_count directly
    page_count = property(get_page_count, set_page_count)

    # method required by the tests
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
