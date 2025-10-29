#!/usr/bin/env python3
import os

def is_running_as_root():
    if os.geteuid() == 0:
        return True
    return False