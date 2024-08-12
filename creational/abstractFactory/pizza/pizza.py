from abc import abstractmethod, ABC
from typing import List

from creational.abstractFactory.ingredients.i_ingredients import IDough, ISauce, IVeggies, ICheese, IPepperoni, IClams


# Product Class

class Pizza(ABC):
    def __init__(self):
        self.name: str = ''
        self.dough: IDough = IDough()
        self.sauce: ISauce = ISauce()
        self.veggies: List[IVeggies] = []
        self.cheese: ICheese = ICheese()
        self.pepperoni: IPepperoni = IPepperoni()
        self.clam: IClams = IClams()

    # We’ve now made the prepare method abstract. This is where we are going to collect the
    # ingredients needed for the pizza, which of course will come from the ingredient factory.
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print(f"Bake for 25 minutes at 360")

    def cut(self):
        print(f"Cutting the pizza into diagonal slices")

    def box(self):
        print(f"Place pizza in official pizza-store box")

    def get_name(self) -> str:
        return self.__class__.__name__
