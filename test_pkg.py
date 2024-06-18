#!/usr/bin/env python3

import pytest

from pkg import init_repo_db, get_pkg_state, do_list, do_install, do_uninstall

def test_package():
    repo = init_repo_db("repo.db")
    assert repo == {'a': ['b', 'c', 'd'], 'd': ['e', 'f'], 'f': ['g']}
    pkg_state = get_pkg_state("tmp_pkgs.db")
    assert pkg_state == set()
    do_install(repo,'a',pkg_state)
    assert pkg_state == {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    do_uninstall(repo,'g',pkg_state)
    assert pkg_state == {'b', 'c', 'e'}
    do_install(repo,'d',pkg_state)
    assert pkg_state == {'b', 'c', 'd', 'e', 'f', 'g'}
    do_uninstall(repo,'e',pkg_state)
    assert pkg_state == {'b', 'c', 'f', 'g'}
    do_uninstall(repo,'g',pkg_state)
    assert pkg_state == {'b', 'c'}
    do_uninstall(repo,'c',pkg_state)
    assert pkg_state == {'b'}
    do_uninstall(repo,'b',pkg_state)
    assert pkg_state == set()
    do_install(repo,'f',pkg_state)
    assert pkg_state == {'f', 'g'}
