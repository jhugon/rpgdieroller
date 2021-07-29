#!/usr/bin/env python3

import random
from blessings import Terminal
import importlib.resources
import csv

TERM_FORMATTING=True
term = Terminal()

class TermSilly:
  def __init__(self):
    self.bold = ""
    self.normal = ""

def disable_term_formatting():
    global TERM_FORMATTING
    global term
    TERM_FORMATTING = False
    term = TermSilly()

def OracleYesNo():
    choices = [
        "Yes and...",
        "Yes but...",
        "No but...",
        "No and...",
    ]
    return random.choice(choices)

def IronswornPayThePrice():
    print(importlib.resources.read_text("rpgdieroller","ironsworndata.paytheprice.csv"))
    with importlib.resources.open_text("rpgdieroller","ironsworndata.paytheprice.csv") as data_file:
        data_reader = csv.reader(data_file,delimiter=",",quatechar='"')
        for row in data_reader:
            print(row)

if __name__ == "__main__":

    for i in range(10):
        print(OracleYesNo())
    IronswornPayThePrice()
