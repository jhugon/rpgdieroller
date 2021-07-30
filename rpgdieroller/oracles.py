#!/usr/bin/env python3

import random
from blessings import Terminal
import importlib.resources
import importlib_resources
import rpgdieroller
from rpgdieroller import ironsworndata
import rpgdieroller.ironsworndata
import csv

def OracleYesNo():
    choices = [
        "Yes and...",
        "Yes but...",
        "No but...",
        "No and...",
    ]
    return random.choice(choices)

def _loadTable(submodule,table_path):
    frequencies = []
    values = []
    single_col = False
    #with open(table_path) as data_file:
    #with importlib.resources.open_text("rpgdieroller.ironsworndata",table_path) as data_file:
    with importlib_resources.open_text("rpgdieroller.ironsworndata",table_path) as data_file:
        data_reader = csv.reader(data_file,delimiter=",",quotechar='"')
        for iRow, row in enumerate(data_reader):
            if iRow == 0 and len(row) == 1:
                single_col = True
            if single_col:
                frequencies.append(1)
                values.append(row[0])
            else:
                frequencies.append(float(row[0]))
                values.append(row[1])
    return frequencies, values

def _getEntryFromTable(submodule,table_path):
    frequencies, values = _loadTable(submodule,table_path)
    result_list = random.choices(values,weights=frequencies)
    return result_list[0]

def IronswornPayThePrice():
    return _getEntryFromTable("ironsworndata","paytheprice.csv")

def IronswornCharacter():
    desc = _getEntryFromTable("ironsworndata","character_descriptor.csv")
    disp = _getEntryFromTable("ironsworndata","character_disposition.csv")
    role = _getEntryFromTable("ironsworndata","character_role.csv")
    goal = _getEntryFromTable("ironsworndata","character_goal.csv")
    ironlandername = _getEntryFromTable("ironsworndata","ironlander_names.csv")
    elfname = _getEntryFromTable("ironsworndata","elf_names.csv")
    return f"{desc}, {disp} {role} wants to {goal} named {ironlandername} (human) or {elfname} (elf)"

def IronswornActionTheme():
    action = _getEntryFromTable("ironsworndata","action.csv")
    theme = _getEntryFromTable("ironsworndata","theme.csv")
    return f"{action} {theme}"

def IronswornLocation():
    loc = _getEntryFromTable("ironsworndata","location.csv")
    desc = _getEntryFromTable("ironsworndata","location_descriptor.csv")
    return f"{desc} {loc}"


if __name__ == "__main__":

    for i in range(10):
        print(OracleYesNo())
    print("\nPay the Price:\n==========================================")
    for i in range(30):
        print(IronswornPayThePrice())

    print("\nCharacter:\n==========================================")
    for i in range(30):
        print(IronswornCharacter())

    print("\nAction-Theme:\n==========================================")
    for i in range(30):
        print(IronswornActionTheme())

    print("\nLocation:\n==========================================")
    for i in range(30):
        print(IronswornLocation())
