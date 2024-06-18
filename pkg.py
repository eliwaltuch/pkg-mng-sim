#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: pkg {install PKG|uninstall PKG|list}")
        return
    cmd = sys.argv[1]
    match cmd:
        case "install":
            print("Usage: install PKG")
        case "uninstall":
            print("Usage: uninstall PKG")
        case "list":
            print("Usage: list")
        case "help":
            print("Usage: pkg {install PKG|uninstall PKG|list}")
            return
        case _:
            print("Invalid argument:", cmd ,"\nUsage: pkg {install PKG|uninstall PKG|list}")
            return

if __name__ == '__main__':
    main()
