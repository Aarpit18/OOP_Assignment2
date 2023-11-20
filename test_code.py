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