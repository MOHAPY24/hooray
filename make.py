#!/usr/bin/env python3
import os
import json, time
from colorama import init, Fore 
from tqdm import tqdm
init(True)


with open("validrepos.json", 'r') as f:
    data = json.loads(f.read())

def make(package_name):
    if package_name in data:
        print(Fore.GREEN + f"[+] package: '{package_name}' found in DPUR")
        cmd = input("[/] install? [Y/n]: ").lower()
        if cmd == "" or cmd == " ":
            cmd = "y"
        if cmd == "y":
            print(Fore.GREEN + f"[+] Installing '{package_name}'")
            for i in tqdm(range(1)):
                os.system(f'wget {data[package_name]} -O /tmp/{package_name}.deb > /dev/null 2>&1')
                os.system(f"sudo apt install -y /tmp/{package_name}.deb > /dev/null 2>&1")
                time.sleep(0.5)
            print(Fore.GREEN + f"[+] package: '{package_name}' installed.")
            os.system("sudo rm -rf /tmp/*")
            exit(0)
        else:
            exit(0)
    else:
        print(Fore.RED + f"[X] package: {package_name} is not a valid DPUR package.")
        exit(1)

