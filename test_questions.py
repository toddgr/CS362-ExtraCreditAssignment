"""
Grace Todd
CS 362: Software Engineering II
Spring 2021
EXTRA CREDIT ASSIGNMENT PYTEST FUNCTION
"""


import pytest
import Question1
import Question3


def test_question1_1():
    assert "Grace is name My" == Question1.reverseSentence("My name is Grace")


def test_question1_2():
    assert "mean you do What" == Question1.reverseSentence("What do you mean")


def test_question1_3():
    assert "sentence another is This" == Question1.reverseSentence("This is another sentence")


def test_question3_1():
    assert [4, 8] == Question3.findSum([1, 2, 3, 4, 5, 6, 7, 8], 12)


def test_question3_2():
    assert [15,13] == Question3.findSum([2, 3, 9, 15, 24, 6, 13, 20], 28)


def test_question3_3():
    assert [10, 5] == Question3.findSum([9, 18, 10, 24, 19, 5], 15)
