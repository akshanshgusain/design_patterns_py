from creational.abstractFactory.ingredients.i_ingredients import *


class ThinCrustIDough(IDough):
    def __init__(self):
        print(f"Preparing Dough: {self.__class__.__name__}")


class ExtraThickIDough(IDough):
    def __init__(self):
        print(f"Preparing Dough: {self.__class__.__name__}")


class MarinaraISauce(ISauce):
    def __init__(self):
        print(f"Preparing Sauce: {self.__class__.__name__}")


class PulmTomatoISauce(ISauce):
    def __init__(self):
        print(f"Preparing Sauce: {self.__class__.__name__}")


class MozzarellaCheese(ICheese):
    def __init__(self):
        print(f"Adding Cheese: {self.__class__.__name__}")


class ReggianoCheese(ICheese):
    def __init__(self):
        print(f"Adding Cheese: {self.__class__.__name__}")


class Garlic(IVeggies):
    def __init__(self):
        print(f"Adding Toppings: {self.__class__.__name__}")


class Onion(IVeggies):
    def __init__(self):
        print(f"Adding Toppings: {self.__class__.__name__}")


class Mushroom(IVeggies):
    def __init__(self):
        print(f"Adding Toppings: {self.__class__.__name__}")


class RedPepper(IVeggies):
    def __init__(self):
        print(f"Adding Toppings: {self.__class__.__name__}")
