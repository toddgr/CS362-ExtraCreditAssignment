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

    def test_question1_2(self):
        sentence = "This is for the extra credit assignment"
        result = "assignment credit extra the for is This"
        self.assertEqual(Question1.reverseSentence(sentence), result)

    def test_question1_3(self):
        sentence = "I like to eat ice cream"
        result = "cream ice eat to like I"
        self.assertEqual(Question1.reverseSentence(sentence), result)

    def test_question3_1(self):
        array = [2, 8, 9, 12, 14, 67]
        target_sum = 21
        self.assertEqual(Question3.findSum(array, target_sum), [9, 12])

    def test_question3_2(self):
        array = [3, 16, 29, 9, 6, 7]
        target_sum = 36
        self.assertEqual(Question3.findSum(array, target_sum), [29, 7])

    def test_question3_3(self):
        array = [23, 14, 16, 10, 2, 7, 9]
        target_sum = 18
        self.assertEqual(Question3.findSum(array, target_sum), [16, 2])

if __name__ == "__main__":
    unittest.main()
