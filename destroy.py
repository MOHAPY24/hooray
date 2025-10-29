#!/usr/bin/env python3
import os
from colorama import init, Fore

init(True)


def destroy(package_name):
    os.system(f"sudo apt remove -y {package_name} > /dev/null 2>&1")
    print(Fore.GREEN + f"[+] package: '{package_name}' removed.")
    quit(0)