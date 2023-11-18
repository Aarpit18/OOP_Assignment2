class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass

class Potion:
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat
    
    def getBoost(self):
        return self.__boost
    
    def setBoost(self, boost):
        self.__boost = boost

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