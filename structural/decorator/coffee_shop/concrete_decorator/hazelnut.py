from structural.decorator.coffee_shop.component.beverage import Beverage
from structural.decorator.coffee_shop.decorator.condiment_decorator import CondimentDecorator


class Hazelnut(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def cost(self) -> float:
        return self.beverage.cost() + 1.0

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Hazelnut"
