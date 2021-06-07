"""
Grace Todd
CS 362: Software Engineering II
Spring 2021

Test file for Extra Credit assignment
"""


import Question1
import unittest


class TestCase(unittest.TestCase):

    def test_question1_1(self):
        sentence = "My name is Grace"
        result = "Grace is name My"
        self.assertEqual(Question1.reverseSentence(sentence), result)


if __name__ == "__main__":
    unittest.main()
