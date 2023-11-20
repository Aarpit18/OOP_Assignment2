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
    """
    assert catalyst_name.getQuality() == 9.7

def testCatalystRefiningTwo():
    catalyst_name = Catalyst("White Berries", 1.2, 9.0)
    catalyst_name.refine()
    """
    Keeping quality value grater than 8.9
    """
    assert catalyst_name.getQuality() == 10