#!/usr/bin/env python3
import subprocess, json
from colorama import init, Fore

init(True)

with open("validrepos.json", 'r') as f:
    data = json.loads(f.read())
    packages = data["stable"]["packages"]



def destroy(package_name):
    if package_name not in packages:
        print(Fore.RED + f"[x] package '{package_name}' is not a valid package.")
        exit(1)
    subprocess.run(f"sudo dpkg -r {package_name} > /dev/null 2>&1")
    print(Fore.GREEN + f"[+] package: '{package_name}' removed.")
    quit(0)