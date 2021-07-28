python3 from vim import *
python3 import rpgdieroller.dierolls as rpgroller
python3 rpgroller.disable_term_formatting()
python3 current.buffer.append("# Dice Roll:")
python3 current.buffer.append("# "+rpgroller.dierollexpr("2d6"))
python3 current.buffer.append("# Fate Dice Roll:")
python3 current.buffer.append("# "+rpgroller.fateroll("+1"))
python3 current.buffer.append("# Count Successful Die Rolls:")
python3 current.buffer.append("# "+rpgroller.rollcountsuccess(10,6,4))
python3 current.buffer.append("# Ironsworn Action Roll:")
python3 current.buffer.append("# "+rpgroller.ironswornaction("+2"))
python3 current.buffer.append("# Ironsworn Progress Roll:")
python3 current.buffer.append("# "+rpgroller.ironswornprogress(8))
