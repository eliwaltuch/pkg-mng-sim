#!/usr/bin/env python3

import sys
import os

def init_repo_db(filename):
    repo = {}
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)

def main():
    if len(sys.argv) < 2:
        print("Usage: pkg {install PKG|uninstall PKG|list}")
        return

    repo = init_repo_db("repo.db")
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
