from enum import Enum
from re import findall

class Element(Enum):
    H = ("Hydrogen", 1)
    He = ("Helium", 2)
    Li = ("Lithium", 3)
    Be = ("Beryllium", 4)
    B = ("Boron", 5)
    C = ("Carbon", 6)
    N = ("Nitrogen", 7)
    O = ("Oxygen", 8)
    F = ("Fluorine", 9)
    Ne = ("Neon", 10)

    def get_name(self):
        return self.value[0]

    def get_atomic_num(self):
        return self.value[1]

    def get_symbol(self):
        return self.name

    def display_info(self):
        return f'Element name: {self.get_name()}\n' \
               f'Element symbol: {self.get_symbol()}\n' \
               f'Atomic number: {self.get_atomic_num()}'


class Chemical:
    def __init__(self, formula):
        self.elements_as_string = findall("[A-Z][^A-Z]*", formula)

        self.elements = []
        for element in self.elements_as_string:
            try:
                exec("self.element = Element.%s" % element)
            except AttributeError:
                self.element = None
            self.elements.append(self.element)

    def __repr__(self):
        return str(self.get_elements())

    def get_elements(self):
        return self.elements