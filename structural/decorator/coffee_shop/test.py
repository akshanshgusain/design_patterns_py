from structural.decorator.coffee_shop.component.beverage import Beverage
from structural.decorator.coffee_shop.concrete_components.espresso import Espresso
from structural.decorator.coffee_shop.concrete_decorator.Mocha import Mocha
from structural.decorator.coffee_shop.concrete_decorator.Whip import Whip
from structural.decorator.coffee_shop.concrete_decorator.hazelnut import Hazelnut

if __name__ == "__main__":
    beverage: Beverage = Espresso()
    print(f"{beverage.get_description()} + ${beverage.cost()}")

    beverage = Whip(beverage)

    print(f"{beverage.get_description()} + ${beverage.cost()}")

    beverage = Mocha(beverage)
    print(f"{beverage.get_description()} + ${beverage.cost()}")

    beverage = Hazelnut(beverage)
    print(f"{beverage.get_description()} + ${beverage.cost()}")

