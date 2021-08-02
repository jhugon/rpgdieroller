py3 import rpgdieroller.vim as rpgroller

function Roll(args)
    py3 rpgroller.roll()
endfunction

function RollCountSuccess(args)
    py3 rpgroller.rollcountsuccess()
endfunction

function RollFate(args)
    py3 rpgroller.rollfate()
endfunction

function IronswornAction(args)
    py3 rpgroller.ironswornaction()
endfunction

function IronswornProgress(args)
    py3 rpgroller.ironswornprogress()
endfunction

command -nargs=+ Roll :call Roll("<args>")
command -nargs=* RollCountSuccess :call RollCountSuccess("<args>")
command -nargs=* RollFate :call RollFate("<args>")
command -nargs=* IronswornAction :call IronswornAction("<args>")
command -nargs=+ IronswornProgress :call IronswornProgress("<args>")

command OracleYesNo :py3 rpgroller.OracleYesNo()
command IronswornPaythePrice :py3 rpgroller.IronswornPayThePrice()
command IronswornCharacterOracle :py3 rpgroller.IronswornCharacterOracle()
command IronswornActionThemeOracle :py3 rpgroller.IronswornActionThemeOracle()
command IronswornLocationOracle :py3 rpgroller.IronswornLocationOracle()
command IronswornSettlementOracle :py3 rpgroller.IronswornSettlementOracle()
command IronswornCombatActionOracle :py3 rpgroller.IronswornCombatActionOracle()
command IronswornChallengeRankOracle :py3 rpgroller.IronswornChallengeRankOracle()
command IronswornMysticBacklashOracle :py3 rpgroller.IronswornMysticBacklashOracle()
command IronswornMajorPlotTwistOracle :py3 rpgroller.IronswornMajorPlotTwistOracle()
