"""
Most functions in here when used in vim, expect vim functions to have argument named args
"""

import rpgdieroller.dierolls as rpgroller
import rpgdieroller.oracles as oracles
import vim
import sys

def _helper():
    args = vim.eval("a:args")
    print(args)
    rpgroller.disable_term_formatting()
    cur_col = vim.current.window.cursor[0]
    return args, cur_col

def _update_cursor(shift):
    pos = vim.current.window.cursor
    pos = (pos[0]+shift,pos[1])
    vim.current.window.cursor = pos

def roll():
    args, cur_col = _helper()
    lines = []
    lines.append("# Dice Roll:")
    lines.append("# "+rpgroller.dierollexpr(args))
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def rollcountsuccess():
    args, cur_col = _helper()
    arglist = args.split(" ")
    if len(arglist) != 3:
        print(f"Error: must use 3 int arguments: <n_dice> <n_sides> <n_for_success>",file=sys.stderr)
        return
    n_dice = arglist[0]
    n_sides = arglist[1]
    n_for_success = arglist[2]
    try:
        n_dice = int(n_dice)
    except ValueError:
        print(f"Error: 1st arg n_dice must be convertable to int, not '{n_dice}'",file=sys.stderr)
        return
    try:
        n_sides = int(n_sides)
    except ValueError:
        print(f"Error: 1st arg n_sides must be convertable to int, not '{n_sides}'",file=sys.stderr)
        return
    try:
        n_for_success = int(n_for_success)
    except ValueError:
        print(f"Error: 1st arg n_for_success must be convertable to int, not '{n_for_success}'",file=sys.stderr)
        return
    rpgroller.disable_term_formatting()
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Count Successful Die Rolls:")
    lines.append("# "+rpgroller.rollcountsuccess(n_dice,n_sides,n_for_success))
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def rollfate():
    args, cur_col = _helper()
    lines = []
    lines.append("# Fate Dice Roll:")
    lines.append("# "+rpgroller.fateroll(args))
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def ironswornaction():
    args, cur_col = _helper()
    lines = []
    lines.append("# Ironsworn Action Roll:")
    lines.append("# "+rpgroller.ironswornaction(args))
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def ironswornprogress():
    n_progress = vim.eval("a:args")
    print(n_progress)
    try:
        n_progress = int(n_progress)
    except ValueError:
        print(f"Error: argument must be convertable to a single int not '{n_progress}'",file=sys.stderr)
        return
    rpgroller.disable_term_formatting()
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn Progress Roll:")
    lines.append("# "+rpgroller.ironswornprogress(n_progress))
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def OracleYesNo():
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Simple oracle roll:")
    lines.append("# "+oracles.OracleYesNo())
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def IronswornPayThePrice():
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn pay the price:")
    lines.append("# "+oracles.IronswornPayThePrice())
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def IronswornCharacterOracle():
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn character oracle:")
    lines.append("# "+oracles.IronswornCharacter())
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def IronswornActionThemeOracle():
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn action-theme oracle:")
    lines.append("# "+oracles.IronswornActionTheme())
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def IronswornLocationOracle():
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn location oracle:")
    lines.append("# "+oracles.IronswornLocation())
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))
