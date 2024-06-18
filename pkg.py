#!/usr/bin/env python3

import sys

cmd = sys.argv[1]
match cmd:
    case "install":
        print("Usage: install PKG")
    case "uninstall":
        print("Usage: uninstall PKG")
    case "list":
        print("Usage: list")
    case _:
        print("Usage: pkg {install PKG|uninstall PKG|list}")
