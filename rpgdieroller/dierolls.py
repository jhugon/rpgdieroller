#!/usr/bin/env python3

from random import randint
from blessings import Terminal
import re

TERM_FORMATTING = True
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


def convstr(x):
    return [str(y) for y in x]


def rolldie(n_sides):
    return randint(1, n_sides)


def rolldice(n_dice, n_sides):
    result = 0
    for i in range(n_dice):
        result += rolldie(n_sides)
    return result


def rollfatedice(n_dice=4):
    return [randint(-1, 1) for i in range(n_dice)]


def parser(inputstr):
    inputstr = inputstr.replace("-", "+-")
    substrs = inputstr.split("+")
    parsed_atoms = []
    for substr in substrs:
        if re.fullmatch(r"\s*", substr):
            continue
        nummatch = re.fullmatch(r"\s*(-*)\s*(\d+)\s*", substr)
        if nummatch:
            sign = nummatch.group(1)
            num = nummatch.group(2)
            if len(sign) > 0:
                sign = sign[0]
            num = int(sign + num)
            parsed_atoms.append(num)
        else:
            dicematch = re.fullmatch(r"\s*(-*)\s*(\d*)[dD](\d+)\s*", substr)
            if dicematch:
                sign = dicematch.group(1)
                numdice = dicematch.group(2)
                numsides = dicematch.group(3)
                parsed_atoms.append(sign + numdice + "d" + numsides)
            else:
                raise Exception(f"Error: couldn't parse '{substr}'")
    result = []
    for atom in parsed_atoms:
        if type(atom) == str:
            dicematch = re.fullmatch(r"\s*(-*)\s*(\d*)[dD](\d+)\s*", atom)
            if dicematch:
                sign = dicematch.group(1)
                try:
                    numdice = int(dicematch.group(2))
                except ValueError:
                    numdice = 1
                numsides = int(dicematch.group(3))
                roll = rolldice(numdice, numsides)
                if len(sign) > 0:
                    roll = -roll
                result.append(roll)
            else:
                raise BaseException(f"Error: couldn't parse '{substr}' in rolling code")
        else:
            result.append(atom)
    return parsed_atoms, result


def resultprinter(parsed_expr, result):
    resultsum = sum(result)
    if len(result) > 1 and (str in [type(x) for x in parsed_expr]):
        return "{t.bold}{0}{t.normal} = {1} = {2}".format(
            resultsum,
            " + ".join(convstr(result)),
            " + ".join(convstr(parsed_expr)),
            t=term,
        )
    elif len(result) > 1:
        return "{t.bold}{0}{t.normal} = {1}".format(
            resultsum,
            " + ".join(convstr(result)),
            " + ".join(convstr(parsed_expr)),
            t=term,
        )
    elif str in [type(x) for x in parsed_expr]:
        return "{t.bold}{0}{t.normal} = {2}".format(
            resultsum,
            " + ".join(convstr(result)),
            " + ".join(convstr(parsed_expr)),
            t=term,
        )
    else:
        return "{t.bold}{0}{t.normal}".format(
            resultsum,
            " + ".join(convstr(result)),
            " + ".join(convstr(parsed_expr)),
            t=term,
        )


def dierollexpr(x):
    exprs = x.split(",")
    resultstr = ""
    nexprs = len(exprs)
    if nexprs > 1:
        resultstr = "("
    for i, expr in enumerate(exprs):
        parsed_expr, result = parser(expr)
        resultstr += resultprinter(parsed_expr, result)
        if i + 1 < nexprs:
            resultstr += ") , ("
        elif nexprs > 1:
            resultstr += ")"
    return resultstr


def fateroll(modifiers="", n_dice=4):
    rolls = rollfatedice(n_dice)
    roll_sum = sum(rolls)
    modifiers_parsed, modifier_results = parser(modifiers)
    modifier_results_sum = sum(modifier_results)
    total_sum = roll_sum + modifier_results_sum
    if len(modifier_results) > 0:
        return (
            "{t.bold}{0}{t.normal} = {1} + {2} = ({3}) + {4} = {n_dice}dF + {5}".format(
                total_sum,
                roll_sum,
                modifier_results_sum,
                " + ".join(convstr(rolls)),
                " + ".join(convstr(modifier_results)),
                " + ".join(convstr(modifiers_parsed)),
                t=term,
                n_dice=n_dice,
            )
        )
    else:
        return "{t.bold}{0}{t.normal} = ({3}) = {n_dice}dF".format(
            total_sum,
            roll_sum,
            modifier_results_sum,
            " + ".join(convstr(rolls)),
            " + ".join(convstr(modifier_results)),
            " + ".join(convstr(modifiers_parsed)),
            t=term,
            n_dice=n_dice,
        )


def rollcountsuccess(n_dice, n_sides, n_for_success):
    """
    You must roll n_for_success or greater (>=) to succeed
    """
    rolls = [rolldie(n_sides) for i in range(n_dice)]
    successes = [1 if x >= n_for_success else 0 for x in rolls]
    n_successes = sum(successes)
    s = ""
    if n_successes > 1:
        s = "es"
    return "{t.bold}{0}{t.normal} Success{s} for {n_dice}d{n_sides} >= {n_for_success}, rolls: ({1})".format(
        n_successes,
        ", ".join(convstr(rolls)),
        t=term,
        n_dice=n_dice,
        n_sides=n_sides,
        n_for_success=n_for_success,
        s=s,
    )


def ironswornaction(modifiers=""):
    """
    The argument is just modifiers added to your action die
    """
    t = term
    modifiers_parsed, modifier_results = parser(modifiers)
    if len(modifiers_parsed) == 0:
        modifiers_parsed = ["0"]
    action_roll = rolldie(6)
    action_modified = action_roll + sum(modifier_results)
    challenge_rolls = [rolldie(10) for x in range(2)]
    successes = [1 if action_modified > x else 0 for x in challenge_rolls]
    nsuccesses = sum(successes)
    if nsuccesses == 2:
        result = "Strong hit"
    elif nsuccesses == 1:
        result = "Weak hit"
    else:
        result = "Miss"
    return f"{t.bold}{result:11}{t.normal} action die: {action_roll:1} + mods: {' + '.join(convstr(modifiers_parsed)):7} = {t.bold}{action_modified:2}{t.normal} vs challenge dice: {challenge_rolls[0]:2}, {challenge_rolls[1]:2}"


def ironswornprogress(progress):
    """
    The progress argument is how many filled boxes you have on your progress track
    Two d10s are rolled and compared to this target number.
    """
    t = term
    challenge_rolls = [rolldie(10) for x in range(2)]
    successes = [1 if progress > x else 0 for x in challenge_rolls]
    nsuccesses = sum(successes)
    if nsuccesses == 2:
        result = "Strong hit"
    elif nsuccesses == 1:
        result = "Weak hit"
    else:
        result = "Miss"
    return f"{t.bold}{result:11}{t.normal} progress {progress:2} vs challenge dice: {challenge_rolls[0]:2}, {challenge_rolls[1]:2}"


if __name__ == "__main__":
    disable_term_formatting()
    print(dierollexpr("50d23 "))
    print(dierollexpr("0"))
    print(dierollexpr("-3"))
    print(dierollexpr("+3"))
    print(dierollexpr("+3-2+6+d4"))
    print(dierollexpr("    -3  +  5d6-3+4+2d2-5d200      +    -   2000d1000-0d0"))
    print(dierollexpr("2D20+3-1"))
    print(dierollexpr("d6+3,d10,d10"))
    print(dierollexpr("d6+3,d10,d10,-3,3"))
    print(fateroll())
    print(fateroll("d4-2"))
    print(fateroll("d4"))
    print(fateroll("-d4"))
    print(fateroll("+4"))
    print(fateroll("-2"))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(4, 6, 4))
    print(rollcountsuccess(5, 6, 4))
    print(rollcountsuccess(6, 6, 4))
    print(rollcountsuccess(7, 6, 4))
    print(rollcountsuccess(20, 6, 4))
    print(rollcountsuccess(50, 6, 4))
    print(rollcountsuccess(50, 6, 4))
    print(rollcountsuccess(50, 6, 4))
    print(rollcountsuccess(50, 6, 4))
    print(rollcountsuccess(50, 6, 4))
    print(rollcountsuccess(1, 20, 15))
    print(ironswornprogress(10))
    print(ironswornprogress(4))
    print(ironswornprogress(4))
    print(ironswornprogress(3))
    print(ironswornprogress(7))
    print(ironswornaction())
    print(ironswornaction("+2"))
    print(ironswornaction("0"))
    print(ironswornaction("+2-4"))
    print(ironswornaction("+4"))
