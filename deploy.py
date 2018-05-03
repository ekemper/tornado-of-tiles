from os import system
import sys
mess = sys.argv[1]
cmd = "git add . && git commit -m '" + mess + "' && git push"
system(cmd)
