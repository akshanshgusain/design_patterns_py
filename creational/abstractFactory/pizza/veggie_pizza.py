from creational.abstractFactory.pizza.pizza import Pizza
from creational.abstractFactory.ingredients.factories.i_pizza_ingredient_factory import IPizzaIngredientFactory


class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory: IPizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.__class__.__name__}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

