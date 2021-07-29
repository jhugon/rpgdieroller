py3 import rpgdieroller.vim as rpgroller

function Roll(args)
    py3 rpgroller.roll()
endfunction

function RollCountSuccess(n_dice,n_sides,n_for_success)
    py3 rpgroller.rollcountsuccess()
endfunction

function RollFate(args)
    py3 rpgroller.rollfate()
endfunction

function IronswornAction(args)
    py3 rpgroller.ironswornaction()
endfunction

function IronswornProgress(n_progress)
    py3 rpgroller.ironswornprogress()
endfunction

command -nargs=+ Roll :call Roll("<args>")
command -nargs=+ RollCountSuccess :call RollCountSuccess("<n_dice>","<n_sides>","<n_for_success>")
command -nargs=* RollFate :call RollFate("<args>")
command -nargs=* IronswornAction :call IronswornAction("<args>")
command -nargs=1 IronswornProgress :call IronswornProgress("<n_progress>")
