from enum import Enum


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
