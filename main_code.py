class Laboratory:
    
class Alchemist:
    def __init__(self):
        self.__attack = 0
        self.__strength = 0
        self.__denfense = 0
        self.__magic = 0
        self.__range = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes: []

    def getLaboratory(self):
        return self.__laboratory
    
    def getRecipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagent(self):
        pass