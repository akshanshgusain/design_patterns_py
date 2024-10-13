from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):

    # prepare_recipe is the Template method
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self):
        print("boiling water")

    def pour_in_cup(self):
        print("pour in cup")


class Tea(CaffeineBeverage):
    def brew(self):
        print("steeping the tea")

    def add_condiments(self):
        print("adding cardamom")


class Coffee(CaffeineBeverage):
    def brew(self):
        print("dripping coffee through filter")

    def add_condiments(self):
        print("adding sugar and cream")
