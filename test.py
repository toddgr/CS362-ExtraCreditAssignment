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
        self.assertEqual(Question1.reverseSentence("My name is Grace"), "Grace is name My")

if __name__ == "__main__":
    unittest.main()
