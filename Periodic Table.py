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
        self.elements = findall("[A-Z][^A-Z]*", formula)
        self.element_freq = {}

        for element in self.elements:
            if "^" in element:
                freq = int(element[element.index("^") + 1:])
                element = element[:element.index("^")]
            else:
                freq = 1

            if element in self.element_freq:
                self.element_freq[element] += freq
            else:
                self.element_freq[element] = freq

        self.elements = []
        for item in self.element_freq.items():
            for i in range(item[1]):
                self.elements.append(item[0])

        self.elements_obj = []
        for element in self.elements:
            try:
                exec("self.element = Element.%s" % element)
            except AttributeError:
                self.element = None
            self.elements_obj.append(self.element)

    def __repr__(self):
        return str([element.get_symbol() for element in self.get_elements()])

    def get_elements(self):
        return self.elements_obj


chem = Chemical("H^4O^2F^1Ne^3")
print(chem)