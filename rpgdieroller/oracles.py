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

def _loadTable(table_path):
    #with importlib.resources.open_text("rpgdieroller",table_path) as data_file:
    frequencies = []
    values = []
    with open(table_path) as data_file:
        data_reader = csv.reader(data_file,delimiter=",",quotechar='"')
        for row in data_reader:
            frequencies.append(float(row[0]))
            values.append(row[1])
    return frequencies, values

def IronswornPayThePrice():
    frequencies, values = _loadTable("ironsworndata/paytheprice.csv")
    result_list = random.choices(values,weights=frequencies)
    return result_list[0]

if __name__ == "__main__":

    for i in range(10):
        print(OracleYesNo())
    for i in range(30):
        print(IronswornPayThePrice())
