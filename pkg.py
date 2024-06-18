#!/usr/bin/env python3

import sys
import os

def init_repo_db(filename):
    repo = {}
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            pkg, deps = line.split(':')
            repo[pkg.strip()] = [dep.strip() for dep in deps.split()]
    return repo

def get_pkg_state(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as file:
        return set(line.strip() for line in file)

def do_list(pkgs):
    for pkg in pkgs:
        print(pkg)

def main():
    if len(sys.argv) < 2:
        print("Usage: pkg {install PKG|uninstall PKG|list}")
        return

    repo = init_repo_db("repo.db")
    pkg_state = get_pkg_state("pkgs.db")
    cmd = sys.argv[1]
    match cmd:
        case "install":
            print("Usage: install PKG")
        case "uninstall":
            print("Usage: uninstall PKG")
        case "list":
            do_list(pkg_state)
        case "help":
            print("Usage: pkg {install PKG|uninstall PKG|list}")
            return
        case _:
            print("Invalid argument:", cmd ,"\nUsage: pkg {install PKG|uninstall PKG|list}")
            return

if __name__ == '__main__':
    main()
