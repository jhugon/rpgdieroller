#!/usr/bin/env python3

import random
from blessings import Terminal
import sys

if sys.version_info < (3, 9):
    import importlib_resources as implibresources
else:
    import importlib.resources as implibresources
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


def _loadTable(submodule, table_path):
    frequencies = []
    values = []
    single_col = False
    with implibresources.open_text(
        "rpgdieroller.ironsworndata", table_path
    ) as data_file:
        data_reader = csv.reader(data_file, delimiter=",", quotechar='"')
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


def _getEntryFromTable(submodule, table_path, cum_weights=False):
    frequencies, values = _loadTable(submodule, table_path)
    result_list = None
    if cum_weights:
        frequencies = [x - 1 for x in frequencies]
        result_list = random.choices(values, cum_weights=frequencies)
    else:
        result_list = random.choices(values, weights=frequencies)
    return result_list[0]


def IronswornPayThePrice():
    return _getEntryFromTable("ironsworndata", "paytheprice.csv")


def IronswornCharacter():
    desc = _getEntryFromTable("ironsworndata", "character_descriptor.csv")
    disp = _getEntryFromTable("ironsworndata", "character_disposition.csv")
    role = _getEntryFromTable("ironsworndata", "character_role.csv")
    goal = _getEntryFromTable("ironsworndata", "character_goal.csv")
    ironlandername = _getEntryFromTable("ironsworndata", "ironlander_names.csv")
    elfname = _getEntryFromTable("ironsworndata", "elf_names.csv")
    giantname = _getEntryFromTable("ironsworndata", "giant_names.csv")
    varouname = _getEntryFromTable("ironsworndata", "varou_names.csv")
    trollname = _getEntryFromTable("ironsworndata", "troll_names.csv")
    return f"{desc}, {disp} {role} wants to {goal} named {ironlandername} (human), {elfname} (elf), {giantname} (giant), {varouname} (varou), or {trollname} (troll)"


def IronswornActionTheme():
    action = _getEntryFromTable("ironsworndata", "action.csv")
    theme = _getEntryFromTable("ironsworndata", "theme.csv")
    return f"{action} {theme}"


def IronswornLocation():
    loc = _getEntryFromTable("ironsworndata", "location.csv")
    desc = _getEntryFromTable("ironsworndata", "location_descriptor.csv")
    return f"{desc} {loc}"


def IronswornSettlement():
    pre = _getEntryFromTable("ironsworndata", "settlement_name_prefix.csv")
    suf = _getEntryFromTable("ironsworndata", "settlement_name_suffix.csv")
    trouble = _getEntryFromTable("ironsworndata", "settlement_trouble.csv")
    return f"{trouble} in {pre}{suf}"


def IronswornCombatAction():
    return _getEntryFromTable("ironsworndata", "combat_actions.csv", True)


def IronswornChallengeRank():
    return _getEntryFromTable("ironsworndata", "challenge_rank.csv", True)


def IronswornMysticBacklash():
    return _getEntryFromTable("ironsworndata", "mystic_backlash.csv", True)


def IronswornMajorPlotTwist():
    return _getEntryFromTable("ironsworndata", "major_plot_twist.csv")


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

    print("\nSettlment:\n==========================================")
    for i in range(30):
        print(IronswornSettlement())

    print("\nCombat Action:\n==========================================")
    for i in range(30):
        print(IronswornCombatAction())

    print("\nChallenge Rank:\n==========================================")
    for i in range(30):
        print(IronswornChallengeRank())

    print("\nCombat Action:\n==========================================")
    for i in range(30):
        print(IronswornMysticBacklash())

    print("\nMajor Plot Twist:\n==========================================")
    for i in range(30):
        print(IronswornMajorPlotTwist())
