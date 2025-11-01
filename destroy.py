#!/usr/bin/env python3
import os, json
from colorama import init, Fore

init(True)

with open("validrepos.json", 'r') as f:
    data = json.loads(f.read())



def destroy(package_name):
    if package_name not in data:
        print(Fore.RED + f"[x] package '{package_name}' is not a valid package.")
        exit(1)
    os.system(f"sudo dpkg -r {package_name} > /dev/null 2>&1")
    print(Fore.GREEN + f"[+] package: '{package_name}' removed.")
    quit(0)