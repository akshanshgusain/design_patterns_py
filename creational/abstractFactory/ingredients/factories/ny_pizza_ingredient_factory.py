from creational.abstractFactory.ingredients.factories.i_pizza_ingredient_factory import *
from creational.abstractFactory.ingredients.ingredients import *


class NYPizzaIngredientFactory(IPizzaIngredientFactory):

    def create_dough(self) -> IDough:
        return ThinCrustIDough()

    def create_sauce(self) -> ISauce:
        return MarinaraISauce()

    def create_cheese(self) -> ICheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[IVeggies]:
        veggies: List[IVeggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> IPepperoni:
        return IPepperoni()

    def create_clam(self) -> IClams:
        return IClams()