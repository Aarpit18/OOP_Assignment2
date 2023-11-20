"""
File Name: main_code.py
Description: Assignment 2 main code
Name: Aarpit Mangla
Student ID: manay087
email: manay087@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest

from main_code import *

"""
Testing of the first class: Herb
"""

def testHerb():
    herb_name = Herb("Irit", 1.0, True)
    assert herb_name.getName() == "Irit"
    assert herb_name.getPotency() == 1.0
    assert herb_name.getGrimy() == True

def testHerbRefining():
    herb_name = Herb("Irit", 1.0, True)
    herb_name.refine()
    assert herb_name.getPotency() == 1.0 * 2.5
    assert herb_name.getGrimy() == False

"""
Testing of Second class: Catalyst
"""

def testCatalyst():
    catalyst_name = Catalyst("White Berries", 1.2, 2.0)
    assert catalyst_name.getName() == "White Berries"
    assert catalyst_name.getPotency() == 1.2
    assert catalyst_name.getQuality() == 2.0

def testCatalystRefining():
    catalyst_name = Catalyst("White Berries", 1.2, 8.6)
    catalyst_name.refine()
    """
    Keeping quality value less than 8.9

    Got value of 9.7 by adding 1.1 in 8.6
    """
    assert catalyst_name.getQuality() == 9.7

def testCatalystRefiningTwo():
    catalyst_name = Catalyst("White Berries", 1.2, 9.0)
    catalyst_name.refine()
    """
    Keeping quality value grater than 8.9

    Got value of 10 following with the condition that 
    """
    assert catalyst_name.getQuality() == 10

"""
Testing Third Class: SuperPotion
"""

def testSuperPotion():
    herb_name = Herb("Kwuarm", 1.2, True)
    catalyst_name = Catalyst("Limpwurt Root", 3.6, 1.7)
    superpotion_name = SuperPotion("Super Strength", "Strength", 0, herb_name, catalyst_name)
    assert superpotion_name.getName() == "Super Strength"
    assert superpotion_name.getStat() == "Strength"
    assert superpotion_name.getBoost() == 0.00
    assert superpotion_name.getHerb() == herb_name
    assert superpotion_name.getCatalyst() == catalyst_name

def testSuperPotionCalculateBoost():
    herb_name = Herb("Kwuarm", 1.2, True)
    catalyst_name = Catalyst("Limpwurt Root", 3.6, 1.7)
    super_potion_name = SuperPotion("Super Strength", "Strength", 0, herb_name, catalyst_name)
    boost_calculation = super_potion_name.calculateBoost(herb_name, catalyst_name)
    assert boost_calculation == round((herb_name.getPotency()) + (catalyst_name.getPotency() * catalyst_name.getQuality()) * 1.5 , 2)

"""
Testing Fourth Class: ExtremePotion
"""

def testExtremePotion():
    reagent_herb = Herb("Swarf Weed", 2.5, True)
    superpotion_name = SuperPotion("Super Strength", "Strength", 0, Herb("Kwuarm", 1.2, True), Catalyst("Limpwurt Root", 3.6, 1.7))
    extremepotion_name = ExtremePotion("Extreme Strength", "Strength", 0, reagent_herb, superpotion_name)
    assert extremepotion_name.getName() == "Extreme Strength"
    assert extremepotion_name.getStat() == "Strength"
    assert extremepotion_name.getBoost() == 0
    assert extremepotion_name.getReagent() == reagent_herb
    assert extremepotion_name.getPotion() == superpotion_name

def testExtremePotionCalculateBoost():
    reagent_herb = Herb("Swarf Weed", 2.5, True)
    superpotion_name = SuperPotion("Super Strength", "Strength", 0, Herb("Kwuarm", 1.2, True), Catalyst("Limpwurt Root", 3.6, 1.7))
    extremepotion_name = ExtremePotion("Extreme Strength", "Strength", 0, reagent_herb, superpotion_name)
    boost_calculation = extremepotion_name.calculateBoost(reagent_herb, superpotion_name)
    assert boost_calculation == round((reagent_herb.getPotency() * superpotion_name.getBoost()) * 3.0 , 2)

"""
Python Fixtures
"""

@pytest.fixture
def catalyst_name():
    return Catalyst("Limpwurt Root", 3.6, 1.7)

@pytest.fixture
def herb_name():
    return Herb("Kwuarm", 1.2, True)

@pytest.fixture
def superpotion_name():
    return SuperPotion("Super Strength", "Strength", 0, herb_name, catalyst_name)

@pytest.fixture
def extremepotion_name():
    return ExtremePotion("Extreme Strength", "Strength", 0, herb_name, superpotion_name)

"""
Testing Fifth Class: Laboratory
"""

def testLaboratoryAddReagent():
    laboratory = Laboratory()
    amount = 2
    laboratory.addReagent(herb_name, amount)
    """
    amount 2 also refers to the number of elements in the herbs list
    """
    assert len(laboratory._Laboratory__herbs) == 2