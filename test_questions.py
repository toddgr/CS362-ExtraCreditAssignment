"""
Grace Todd
CS 362: Software Engineering II
Spring 2021
EXTRA CREDIT ASSIGNMENT PYTEST FUNCTION
"""
import pytest
import Question1

def test_question1_1():
    assert "Grace is name My" == Question1.reverseSentence("My name is Grace")