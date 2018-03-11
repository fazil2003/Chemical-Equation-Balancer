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
    Na = ("Sodium", 11)
    Mg = ("Magnesium", 12)
    Al = ("Aluminium", 13)
    Si = ("Silicon", 14)
    P = ("Phosphorus", 15)
    S = ("Sulfur", 16)
    Cl = ("Chlorine", 17)
    Ar = ("Argon", 18)
    K = ("Potassium", 19)
    Ca = ("Calcium", 20)
    Sc = ("Scandium", 21)
    Ti = ("Titanium", 22)
    V = ("Vanadium", 23)
    Cr = ("Chromium", 24)
    Mn = ("Manganese", 25)
    Fe = ("Iron", 26)
    Co = ("Cobalt", 27)
    Ni = ("Nickel", 28)
    Cu = ("Copper", 29)
    Zn = ("Zinc", 30)
    Ga = ("Gallium", 31)
    Ge = ("Germanium", 32)
    As = ("Arsenic", 33)
    Se = ("Selenium", 34)
    Br = ("Bromine", 35)
    Kr = ("Krypton", 36)
    Rb = ("Rubidium", 37)
    Sr = ("Strontium", 38)
    Y = ("Yttrium", 39)
    Zr = ("Zirconium", 40)
    Nb = ("Niobium", 41)
    Mo = ("Molybdenum", 42)
    Tc = ("Technetium", 43)
    Ru = ("Ruthenium", 44)
    Rh = ("Rhodium", 45)
    Pd = ("Palladium", 46)
    Ag = ("Silver", 47)
    Cd = ("Cadmium", 48)
    In = ("Indium", 49)
    Sn = ("Tin", 50)
    Sb = ("Antimony", 51)
    Te = ("Tellurium", 52)
    I = ("Iodine", 53)
    Xe = ("Xenon", 54)

    def get_name(self):
        return self.value[0]

    def get_atomic_num(self):
        return self.value[1]

    def get_symbol(self):
        return self.name

    def __repr__(self):
        return f'Element name: {self.get_name()}\n' \
               f'Element symbol: {self.get_symbol()}\n' \
               f'Atomic number: {self.get_atomic_num()}'


class Chemical:
    def __init__(self, formula):
        self.elements = findall("[A-Z][^A-Z]*", formula)
        self.element_freq = {}

        # Making frequency dictionary for elements
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

        # Re-writing self.elements with only the element symbol
        self.elements = []
        for item in self.element_freq.items():
            for i in range(item[1]):
                self.elements.append(item[0])

        # Making self.elements_obj to store actual Element objects instead of strings
        self.elements_obj = []
        for element_name in self.elements:
            if hasattr(Element, element_name):
                self.element = getattr(Element, element_name)
            else:
                raise RuntimeError(f'Unknown element name {element_name}')
            self.elements_obj.append(self.element)

    def __repr__(self):
        return str([element.get_symbol() for element in self.elements_obj])

    def get_elements(self):
        return self.elements_obj


class Reactants:
    def __init__(self, *chemicals):
        self.elements, self.element_freq = Reactants.map_chemicals(chemicals)

    @classmethod
    def map_chemicals(cls, chemicals):
        """
        :param chemicals: A tuple of n chemicals
        :return: array of all of the elements, dictionary of every element to its frequency
        """
        elements = []
        for chemical in chemicals:
            for element in chemical.get_elements():
                elements.append(element)

        element_freq = {}
        for element in elements:
            if element in element_freq:
                element_freq[element] += 1
            else:
                element_freq[element] = 1

        return elements, element_freq

    def __repr__(self):
        """
        Repr method for Reactants
        :return: A visual mapping of each element to its frequency
        """
        output = ""
        for element in self.element_freq:
            output += f"{element.get_symbol()} = {self.element_freq[element]}\n"
        return output


c1 = Chemical("NaOH")
c2 = Chemical("H^2")
reactants = Reactants(c1, c2)
print(reactants)