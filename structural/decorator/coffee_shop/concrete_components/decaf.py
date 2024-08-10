from structural.decorator.coffee_shop.component.beverage import Beverage


class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Decaf"

    def cost(self) -> float:
        return 1.05
