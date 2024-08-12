from creational.abstractFactory.ingredients.factories.chicago_pizza_ingredient_factory import \
    ChicagoPizzaIngredientFactory
from creational.abstractFactory.ingredients.factories.i_pizza_ingredient_factory import IPizzaIngredientFactory
from creational.abstractFactory.pizza.cheese_pizza import CheesePizza
from creational.abstractFactory.pizza.clam_pizza import ClamPizza
from creational.abstractFactory.pizza.pepperoni_pizza import PepperoniPizza
from creational.abstractFactory.pizza.pizza import Pizza
from creational.abstractFactory.pizza_store import PizzaStore
from creational.abstractFactory.pizza.veggie_pizza import VeggiePizza


class ChicagoPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.pizza = None
        self.ingredient_factory: IPizzaIngredientFactory = ChicagoPizzaIngredientFactory()
        # create an ingredient factory

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            self.pizza = CheesePizza(self.ingredient_factory)
        elif pizza_type == "pepperoni":
            self.pizza = PepperoniPizza(self.ingredient_factory)
        elif pizza_type == "clam":
            self.pizza = ClamPizza(self.ingredient_factory)
        elif pizza_type == "veggie":
            self.pizza = VeggiePizza(self.ingredient_factory)
        else:
            self.pizza = CheesePizza(self.ingredient_factory)

        print(f"\nWelcome to {self.__class__.__name__}")
        return self.pizza
