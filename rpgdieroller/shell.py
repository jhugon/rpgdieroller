#!/usr/bin/env python3

from rpgdieroller.dierolls import *
import cmd

class DieRollerShell(cmd.Cmd):

    intro = "Welcome to the Python RPG Die Roller shell. Type help or ? to list commands.\n"
    prompt = "(RPG Die Roller) "
    
    def do_roll(self,arg):
        "Roll the dice for an expression like 'd10+2d6 + 5 - 3' or '5d20+2' or 'd20' or '3d6'. Any number of sides and dice are allowed."
        print(dierollexpr(arg))

    def do_fateroll(self,arg):
        "Roll 4 fate dice. Any argument is the modifier and can be '-4', '6', '+6', and even 'd4+3d6+4-10'."
        print(fateroll(arg))

    def do_countsuccessrolls(self,args):
        "(RPG Die Roller) countsuccessrolls <NDICE> <NSIDES> <NFORSUCCESS>\nRoll NDICE each with NSIDES and count how many of the rolled dice are at least NFORSUCCESS."
        arglist = args.split(" ")
        if len(arglist) != 3:
            print("Error: there must be 3 positive integer arguments")
            return
        argnums = None
        try:
            argnums = [int(x) for x in arglist]
        except ValueError:
            print("Error: there must be 3 positive integer arguments")
            return
        for x in argnums:
            if x <= 0:
                print("Error: there must be 3 positive integer arguments")
                return
        print(rollcountsuccess(*argnums))

    def do_ironsworn(self,args):
        "Do an Ironsworn action roll with the modifiers as arguments '+2 -2' or anything you can put in the roll command"
        print(ironswornaction(args))

    def do_ironswornprogress(self,args):
        "Do an Ironsworn progress roll with the amount of progress as an integer argument '2' or '9'"
        arglist = args.split(" ")
        if len(arglist) != 1:
            print("Error: there must be exactly 1 integer argument")
            return
        argnums = None
        try:
            argnums = [int(x) for x in arglist]
        except ValueError:
            print("Error: there must be exactly 1 integer argument")
            return
        
        print(ironswornprogress(argnums[0]))

    def do_exit(self,_):
        "Exit the shell."
        print("Exiting.")
        return True

    def do_quit(self,_):
        "Exit the shell."
        print("Exiting.")
        return True


if __name__ == "__main__":

    DieRollerShell().cmdloop()
