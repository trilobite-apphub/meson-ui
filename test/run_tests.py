#!/usr/bin/env python3

#
# Troglobyte AppHub:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from code.program import greet


#
# Test cases for this project.
#
def test_basic_assert_works():
    assert True

def test_greet_not_none():
    assert greet() is not None
