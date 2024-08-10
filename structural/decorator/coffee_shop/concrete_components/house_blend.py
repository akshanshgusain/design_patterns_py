from structural.decorator.coffee_shop.component.beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House blend coffee"

    def cost(self) -> float:
        return 0.89
