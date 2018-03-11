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
        return self.get_symbol()


class Chemical:
    def __init__(self, formula):
        self._elements = findall("[A-Z][^A-Z]*", formula)
        self._element_freq = {}
        self.formula = formula

        # Making frequency dictionary for elements
        for element in self._elements:
            if "^" in element:
                freq = int(element[element.index("^") + 1:])
                element = element[:element.index("^")]
            else:
                freq = 1

            if element in self._element_freq:
                self._element_freq[element] += freq
            else:
                self._element_freq[element] = freq

        # Re-writing self.elements with only the element symbol
        self._elements = []
        for item in self._element_freq.items():
            for i in range(item[1]):
                self._elements.append(item[0])

        # Making self.elements_obj to store actual Element objects instead of strings
        self.elements_obj = []
        for element_name in self._elements:
            if hasattr(Element, element_name):
                self.element = getattr(Element, element_name)
            else:
                raise RuntimeError(f'Unknown element name {element_name}')
            self.elements_obj.append(self.element)

    def __repr__(self):
        return self.formula

    def get_elements(self):
        return self.elements_obj


class Reactants:
    def __init__(self, *chemicals):
        self._chemicals = chemicals
        self._elements, self._element_freq = Reactants.map_chemicals(chemicals)

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
        :return: The elements written as a sum
        """
        output = str(self._chemicals[0])
        for chemical in self._chemicals[1:]:
            output += f" + {chemical}"
        return output

    def get_elements(self):
        return self._elements

    def get_element_frequency(self):
        return self._element_freq

    def get_chemicals(self):
        return self._chemicals


class BalancedEquation:
    def __init__(self, reactant_1, reactant_2):
        # If the reactants contain different elements, a ValueError is raised
        if set(reactant_1.get_elements()) != set(reactant_2.get_elements()):
            raise ValueError (f"[{reactant_1}] will never become [{reactant_2}]")

        self._reactant_1 = reactant_1
        self._reactant_2 = reactant_2


c1 = Chemical("O^2")
c2 = Chemical("H^2")
reactant1 = Reactants(c1, c2)

c3 = Chemical("H^2O")
reactant2 = Reactants(c3)

be = BalancedEquation(reactant1, reactant2)