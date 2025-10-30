#!/usr/bin/env python3

import make
import sys
import _utils
import help
from colorama import init, Fore 
init(True)



if not _utils.is_running_as_root():
    print(Fore.RED + "[X] hooray must be ran as root.")
    quit(1)

try:
    sys.argv[1]
except:
    print(Fore.RED + "[X] No arguments provided")
    exit(1)

if __name__ == "__main__":
    if sys.argv[1] == "make":
        make.make(sys.argv[2])
    elif sys.argv[1] == "help": 
        help.help()
    elif sys.argv[1] == "destroy":
        from destroy import destroy
        destroy(sys.argv[2])
    else:
        print(Fore.RED + f"[X] Unknown command '{sys.argv[1]}'.")
        print(Fore.BLUE + "[+] use 'hooray help' for more information.")
        exit(1)
    