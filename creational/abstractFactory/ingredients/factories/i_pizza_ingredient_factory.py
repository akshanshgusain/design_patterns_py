"""
Now we’re going to build a factory to create our ingredients; the factory will be responsible for creating each
ingredient in the ingredient family. In other words, the factory will need to create dough, sauce, cheese, and so
 on... You’ll see how we are going to handle the regional differences shortly.

"""
from abc import abstractmethod
from typing import List
from creational.abstractFactory.ingredients.i_ingredients import *

# Abstract Factory
"""
An Abstract Factory gives us an interface for creating a family of products
"""

"""
Because our code is decoupled from the actual products, we can substitute different factories to get different behaviors
"""


class IPizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> IDough:
        pass

    @abstractmethod
    def create_sauce(self) -> ISauce:
        pass

    @abstractmethod
    def create_cheese(self) -> ICheese:
        pass

    @abstractmethod
    def create_veggies(self) -> List[IVeggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> IPepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> IClams:
        pass
