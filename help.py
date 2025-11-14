#!/usr/bin/env python3

def help():
    print("Hooray - a simple wrapper for installing pre-checked .deb packages from the DPUR (Debian Public User Repository).")
    print("Inspired by the yay AUR helper. Ment to help users of any Debian-based Linux distro install prechecked and open-source .deb packages.")
    print("Ment to be a secondary package manager, not a replacement for apt. Similar on how yay is to pacman.")
    print("Made with <3 by /home/momo / MOHAPY24")
    print("\n\tUsage: sudo hooray <command> <args>")
    print("\n\tCommands:")
    print("\t\tmake <package_name> \t- installs a package from the DPUR (Debian Public User Repository).")
    print("\t\thelp \t\t\t- shows this help message.")
    print("\tdestroy <package_name> \t- uninstalls a package from your system.")
    print("\n\tValid package names can be found in the validrepos.json file.")