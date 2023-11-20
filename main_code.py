from abc import ABC, abstractmethod

class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
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
        if self.__grimy:
            self.setPotency(self.getPotency()*2.5)
            self.__grimy = False
            print(f"{self.getName()} is no longer grimy and Potency is multiplied by 2.5.")

    def getGrimy(self):
        return self.__grimy
    
    def setGrimy(self, grimy):
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality increased to {self.__quality} ")
        elif self.__quality >= 8.9:
            self.__quality = 10
            print(f"Quality set to 10. It cannot be refined further.")

    def getQuality(self):
        return self.__quality
    
class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
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
        boost_calculation = self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5
        return round(boost_calculation, 2)

    def getHerb(self):
        return self.__herb
    
    def getCatalyst(self):
        return self.__catalyst
    
class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def getBoost(self):
        return super().getBoost()
    
    def calculateBoost(self):
        boost_calculation = (self.__reagent.getPotency() * self.__potion.getBoost()) * 3.0
        return round(boost_calculation, 2)

    def getReagent(self):
        return self.__reagent
    
    def getPotion(self):
        return self.__potion
    
class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        if isinstance (primaryIngredient, (Herb, Catalyst)) and isinstance(secondaryIngredient, (Catalyst, Potion)):
            if type == "SuperPotion" and isinstance(primaryIngredient, Herb) and isinstance(secondaryIngredient, Catalyst):
                mixed_potion = SuperPotion(name, stat, primaryIngredient, secondaryIngredient)
            elif type == "ExtremePotion" and (isinstance(primaryIngredient, Herb) or isinstance(primaryIngredient, Catalyst)) and isinstance(secondaryIngredient, Potion):
                mixed_potion = ExtremePotion(name, stat, primaryIngredient, secondaryIngredient)

            mixed_potion.setBoost(mixed_potion.calculateBoost())

            self.__potions.append(mixed_potion)
            print(f"{mixed_potion.getName()} was invented on mixing and was successfully added to the Laboratory")
        else:
            print(f"An error encountered while mixing!")

    def addReagent(self, reagent, amount):
        for _ in range(amount):
            if isinstance (reagent, Herb):
                self.__herbs.append(reagent)
            elif isinstance (reagent, Catalyst):
                self.__catalysts.append(reagent)

    def getHerbs(self):
        return self.__herbs
    
    def getCatalysts(self):
        return self.__catalysts
    
    def getPotions(self):
        return self.__potions
    
class Alchemist:
    def __init__(self):
        self.__attack = 0
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__range = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes = []

    def getLaboratory(self):
        return self.__laboratory
    
    def getRecipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe):
        self.__laboratory.mixPotion(recipe.getName(), recipe.getType(), recipe.getStat(), recipe.getPrimaryIngredient(), recipe.getSecondaryIngredient())

    def drinkPotion(self, potion):
        potion_stats = potion.getStat()
        self.__attack += potion_stats["attack"]
        self.__strength += potion_stats["strength"]
        self.__defense += potion_stats["defense"]
        self.__magic += potion_stats["magic"]
        self.__range += potion_stats["range"]
        self.__necromancy += potion_stats["necromancy"]

    def collectReagent(self, reagent, amount):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagent(self):
        for herb in self.__laboratory.getHerbs():
            herb.refine()
        for catalyst in self.__laboratory.getCatalysts():
            catalyst.refine()