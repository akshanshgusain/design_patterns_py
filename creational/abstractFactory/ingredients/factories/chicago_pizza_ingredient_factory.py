from creational.abstractFactory.ingredients.factories.i_pizza_ingredient_factory import *
from creational.abstractFactory.ingredients.ingredients import *


class ChicagoPizzaIngredientFactory(IPizzaIngredientFactory):

    def create_dough(self) -> IDough:
        return ExtraThickIDough()

    def create_sauce(self) -> ISauce:
        return PulmTomatoISauce()

    def create_cheese(self) -> ICheese:
        return MozzarellaCheese()

    def create_veggies(self) -> List[IVeggies]:
        veggies: List[IVeggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> IPepperoni:
        return IPepperoni()

    def create_clam(self) -> IClams:
        return IClams()