"""
Grace Todd
CS 362: Software Engineering II
Spring 2021

Test file for Extra Credit assignment
"""


import Question1
import Question3
import unittest


class TestCase(unittest.TestCase):

    def test_question1_1(self):
        sentence = "My name is Grace"
        result = "Grace is name My"
        self.assertEqual(Question1.reverseSentence(sentence), result)

    def test_question3_1(self):
        array = [2, 8, 9, 12, 14, 67]
        target_sum = 21
        self.assertEqual(Question3.findSum(array, target_sum), [9, 12])


if __name__ == "__main__":
    unittest.main()
