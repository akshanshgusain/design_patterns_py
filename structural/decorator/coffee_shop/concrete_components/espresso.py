from structural.decorator.coffee_shop.component.beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
