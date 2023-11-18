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

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass

    def getHerb(self):
        return self.__herb
    
    def getCatalyst(self):
        return self.__catalyst
    
class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass

    def getReagent(self):
        return self.__reagent
    
    def getPotion(self):
        return self.__potion
    
class Reagent:
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    def refine(self):
        pass

    def getName(self):
        return self.__name
    
    def getPotency(self):
        return self.__potency
    
    def setPotency(self, potency):
        self.__potency = potency

class Herb(Reagent):
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        if self.__grimy == True:
            print(f"Refining {self.__name}")
            self.setPotency(self.getPotency()*2.5)
            self.__grmiy = False
            print(f"{self.getName()} is no longer grimy and Potency is multiplied by 2.5")

    def getGrimy(self):
        return self.__grmiy
    
    def setGrimy(self, grimy):
        self.__grmiy = grimy

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            print(f"Refining {self.__name}")
            self.__quality += 1.0
            print(f"Quality increased to {self.__quality} ")
        elif self.__quality >= 8.9:
            print(f"Refining {self.__name}")
            self.__quality = 10
            print(f"Quality set to 10. It cannot be refined further.")

    def getQuality(self):
        return self.__quality
    
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