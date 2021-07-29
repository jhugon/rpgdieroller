"""
Most functions in here when used in vim, expect vim functions to have argument named args
"""

import rpgdieroller.dierolls as rpgroller
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
    lines.append("")
    _update_cursor(len(lines))

def rollcountsuccess():
    """
    This function expects the vim function to take 3 arguments named:
    n_dice, n_sides, n_for_success
    """
    n_dice = vim.eval("a:n_dice")
    n_sides = vim.eval("a:n_sides")
    n_for_success = vim.eval("a:n_for_success")
    rpgroller.disable_term_formatting()
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Count Successful Die Rolls:")
    lines.append("# "+rpgroller.rollcountsuccess(n_dice,n_sides,n_for_success))
    lines.append("")
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def rollfate():
    args, cur_col = _helper()
    lines = []
    lines.append("# Fate Dice Roll:")
    lines.append("# "+rpgroller.fateroll(args))
    lines.append("")
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))

def ironswornaction():
    args, cur_col = _helper()
    lines = []
    lines.append("# Ironsworn Action Roll:")
    lines.append("# "+rpgroller.ironswornaction(args))
    lines.append("")
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))
# Fate Dice Roll:
# -2 = (0 + -1 + 0 + -1) = 4dF

# Dice Roll:
# 86 = 14 + 1 + 2 + 59 + -6 + 16 = 3d6 + 1 + 2 + 1d100 + -6 + 1d20

# Fate Dice Roll:
# 5 = 1 + 4 = (1 + -1 + 0 + 1) + 4 = 4dF + 4

# Ironsworn Action Roll:
# Strong hit  action die: 6 + mods: 0       =  6 vs challenge dice:  3,  1
# Ironsworn Action Roll:
# Weak hit    action die: 5 + mods: 4       =  9 vs challenge dice:  5,  9
# Ironsworn Action Roll:
# Weak hit    action die: 2 + mods: 1 + 1   =  4 vs challenge dice:  3,  4



def ironswornprogress():
    """
    This function expects the vim function to take 1 arguments named:
    n_progress
    """
    n_progress = vim.eval("a:n_progress")
    try:
        n_progress = int(n_progress)
    except ValueError:
        print(f"Error: n_progress must be convertable to int not '{n_progress}'",file=sys.stderr)
        return
    rpgroller.disable_term_formatting()
    cur_col = vim.current.window.cursor[0]
    lines = []
    lines.append("# Ironsworn Progress Roll:")
    lines.append("# "+rpgroller.ironswornprogress(n_progress))
    lines.append("")
    vim.current.buffer.append(lines,cur_col)
    _update_cursor(len(lines))
