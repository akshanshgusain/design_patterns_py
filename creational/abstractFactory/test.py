from creational.abstractFactory.chicago_pizza_store import ChicagoPizzaStore
from creational.abstractFactory.ny_pizza_store import NYPizzaStore
from creational.abstractFactory.pizza_store import PizzaStore


if __name__ == "__main__":
    ny_pizza_store: PizzaStore = NYPizzaStore()  # create NY Ingredient Factory inside the constructor
    ny_pizza_store.order_pizza("cheese")
    ny_pizza_store: PizzaStore = ChicagoPizzaStore()  # create NY Ingredient Factory inside the constructor
    ny_pizza_store.order_pizza("cheese")
