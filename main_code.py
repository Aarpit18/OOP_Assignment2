"""
File Name: main_code.py
Description: Assignment 2 main code
Name: Aarpit Mangla
Student ID: manay087
email: manay087@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod

class Reagent(ABC): 
    """
    Abstract Base Class for Reagents
    """
    def __init__(self, name, potency):
        """
        Initialise for Reagent with parameters name and potency

        Parameters:
        - name(str): Name of Reagent
        - potency(float): Potency value of Reagent
        """
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        """
        Abstract method that refines the reagent.
        """
        pass
    
    def getName(self):
        """
        Gets the name of the reagent.
        
        Returns:
        - str: The name of reagent
        """
        return self.__name

    def getPotency(self):
        """
        Gets the potency value of the reagent.
        
        Returns:
        - float: The potency value of reagent.
        """
        return self.__potency

    def setPotency(self, potency):
        """
        Sets the new potency value of the reagent.
        
        Parameters:
        - potency(float): The new potency value of the reagent.
        """
        self.__potency = potency

class Herb(Reagent):
    """
    This Herb class which is type of Reagent, iherits data from reagent class as well.
    """
    def __init__(self, name, potency, grimy):
        """
        Initialise a herb with parameters name, potency and grimy.

        Parameters:
        - name (str): Name of Herb.
        - potency(float): Potency value of herb.
        - grimy(bool): Defines the grimy status of the herb.
        """
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        """
        Refining the herb and sets the potency value and grimy status.
        """
        if self.__grimy:
            self.setPotency(self.getPotency()*2.5)
            self.__grimy = False
            print(f"{self.getName()} is no longer grimy and Potency is multiplied by 2.5.")

    def getGrimy(self):
        """
        Gets the grimy status of herb.
        
        Returns:
        - bool: The grimy status of the herb.
        """
        return self.__grimy
    
    def setGrimy(self, grimy):
        """
        Sets the grimy status of the herb.
        
        Parameters:
        - grimy(bool): The new grimy status is updated.
        """
        self.__grimy = grimy

class Catalyst(Reagent):
    """
    This Catalyst class which is type of Reagent, iherits data from reagent class as well.
    """
    def __init__(self, name, potency, quality):
        """
        Initialise a catalyst with parameters name, potency and quality.

        Parameters:
        - name (str): Name of Catalyst.
        - potency(float): Potency value of Catalyst.
        - quality(float): Quality value of the Catalyst.
        """
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        """
        Refines the catalyst and updates quality:

        If quality is below is 8.9, increase quality by 1.1.
        If quality is above 8.9, sets quality to 10.
        """
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality increased to {self.__quality} ")
        elif self.__quality >= 8.9:
            self.__quality = 10
            print(f"Quality set to 10. It cannot be refined further.")

    def getQuality(self):
        """
        Gets the Catalyst's Quality Value.

        Returns:
        - float: The quality value of the catalyst.
        """
        return self.__quality
    
class Potion(ABC):
    """
    Abstract Base Class for Potion.
    """
    def __init__(self, name, stat, boost):
        """
        Initialise for Reagent with parameters name, stat and boost.

        Parameters:
        - name(str): Name of the potion.
        - stat(str): Stat attribute of the potion.
        - boost(float): Boost value of the potion.
        """
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        """
        Abstract method for calculating boost of the potion.
        """
        pass

    def getName(self):
        """
        Get the Potion Name.

        Returns:
        - str: The name of the potion.
        """
        return self.__name
    
    def getStat(self):
        """
        Gets updated potion stats.

        Returns:
        - str: The stat of the potion.
        """
        return self.__stat

    def getBoost(self):
        """
        Gets the boost value of the potion.

        Returns:
        - float: The boost value of the Potion.
        """
        return self.__boost

    def setBoost(self, boost):
        """
        Sets the new boost value of the potion.

        Parameters:
        - Boost(float): The new boost value of the Potion is updated.
        """
        self.__boost = boost

class SuperPotion(Potion):
    """
    This SuperPotion class which is type of Potion, iherits data from Potion class as well.
    """
    def __init__(self, name, stat, boost, herb, catalyst):
        """
        Initialise for SuperPotion with parameters name, stat, boost, herb and catalyst.

        Parameters:
        - name(str): Name of the potion.
        - stat(str): Stat attribute of the potion.
        - boost(float): Boost value of the potion.
        - herb(Herb): The herb used as an ingredient in the potion.
        - catalyst(Catalyst): The catalyst used as an ingredient in the potion.
        """
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        """
        Calculates the boost value of the potion.

        Returns:
        - float: The calculated boost value of the potion.
        """
        boost_calculation = self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5
        return round(boost_calculation, 2)

    def getHerb(self):
        """
        Gets the herb used as an ingredient in the SuperPotion.

        Returns:
        - Herb: The herb used as an ingredient in the potion.
        """
        return self.__herb
    
    def getCatalyst(self):
        """
        Gets the catalyst used as an ingredient in the SuperPotion.

        Returns:
        - Catalyst: The catalyst used as an ingredient in the potion.
        """
        return self.__catalyst
    
class ExtremePotion(Potion):
    """
    This ExtremePotion class which is type of Potion, iherits data from Potion class as well.
    """
    def __init__(self, name, stat, boost, reagent, potion):
        """
        Initialise for SuperPotion with parameters name, stat, boost, reagent and potion.

        Parameters:
        - name(str): Name of the potion.
        - stat(str): Stat attribute of the potion.
        - boost(float): Boost value of the potion.
        - reagent(Reagent): The reagent used as an ingredient in the potion.
        - potion(Potion): The potion used as an ingredient in the potion.
        """
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion
    
    def calculateBoost(self):
        """
        Calculates the boost value of the potion.

        Returns:
        - float: The calculated boost value of the potion.
        """
        boost_calculation = (self.__reagent.getPotency() * self.__potion.getBoost()) * 3.0
        return round(boost_calculation, 2)

    def getReagent(self):
        """
        Gets the reagent used as an ingredient in the SuperPotion.

        Returns:
        - Reagent: The reagent used as an ingredient in the potion.
        """
        return self.__reagent
    
    def getPotion(self):
        """
        Gets the potion used as an ingredient in the SuperPotion.

        Returns:
        - Potion: The potion used as an ingredient in the potion.
        """
        return self.__potion
    
class Laboratory:
    """
    Class that represents Laboratory for an Alchemist.
    """
    def __init__(self):
        """
        Initialise the laboratory with empty lists of potions, herbs and catalysts.
        """
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """
        Mixing of a potion in the laboratory.

        Parameters:
        - name(str): The name of the potion.
        - type(str): The type of the potion (SuperPotion or ExtremePotion).
        - stat(str): The updated stat of the potion.
        - primaryIngredient (Herb or Catalyst): The primary ingredient of the potion.
        - secondaryIngredient (Catalyst or Potion): The secondary ingredient of the potion.
        """
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
        """
        Add reagents to the laboratory.

        Parameters:
        - reagent(Herb or Catalyst): The reagent that will be added to the laboratory.
        - amount(int): The amount of the reagent that will be added.
        """
        for _ in range(amount):
            if isinstance (reagent, Herb):
                self.__herbs.append(reagent)
            elif isinstance (reagent, Catalyst):
                self.__catalysts.append(reagent)

    def getHerbs(self):
        """
        Gets the list of the herbs available in the laboratory.

        Returns:
        - list: The list of herbs available in the laboratory.
        """
        return self.__herbs
    
    def getCatalysts(self):
        """
        Gets the list of the catalysts available in the laboratory.

        Returns:
        - list: The list of catalysts available in the laboratory.
        """
        return self.__catalysts
    
    def getPotions(self):
        """
        Gets the list of the potions available in the laboratory.

        Returns:
        - list: The list of potions available in the laboratory.
        """
        return self.__potions
    
class Alchemist:
    """
    Class that represents the Alchemist.
    """
    def __init__(self):
        """
        Initialise the Alchemist class with some attributes value and laboratory and recipies list.
        """
        self.__attack = 0
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__range = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes = []

    def getLaboratory(self):
        """
        Gets the laboratory associated with the Alchemist.

        Returns:
        - Laboratory: The laboratory associated with the Alchemist
        """
        return self.__laboratory
    
    def getRecipes(self):
        """
        Gets the laboratory associated with the Alchemist.

        Returns:
        - Laboratory: The laboratory associated with the Alchemist.
        """
        return self.__recipes
    
    def mixPotion(self, recipe):
        """
        Mix a potion in the laboratory based on the given recipe.

        Parameters:
        - recipe(dict): A dictionary containing data about the portion recipe.
        """
        self.__laboratory.mixPotion[recipe.getName(), recipe.getType(), recipe.getStat(), recipe.getPrimaryIngredient(), recipe.getSecondaryIngredient()]

    def drinkPotion(self, potion):
        """
        Drink the portion and adds to the stats as per potion status.

        Parameters:
        - potion(Potion): The potion that is drank.
        """
        potion_stats = potion.getStat()
        self.__attack += potion_stats["attack"]
        self.__strength += potion_stats["strength"]
        self.__defense += potion_stats["defense"]
        self.__magic += potion_stats["magic"]
        self.__range += potion_stats["range"]
        self.__necromancy += potion_stats["necromancy"]

    def collectReagent(self, reagent, amount):
        """
        Collects reagents and add thems to the laboratory.

        Parameters:
        - reagent(Herb or Catalyst): The reagent to collect.
        - amount(int): The amount of reagent to collect and add. 
        """
        self.__laboratory.addReagent(reagent, amount)

    def refineReagent(self):
        """
        Refines all herbs and catalysts in the laboratory.
        """
        for herb in self.__laboratory.getHerbs():
            herb.refine()
        for catalyst in self.__laboratory.getCatalysts():
            catalyst.refine()