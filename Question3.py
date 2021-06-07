"""
Grace Todd
CS 362: Software Engineering II
Spring 2021
EXTRA CREDIT ASSIGNMENT QUESTION 1
Write a program that takes an array
of integers - array and an integer target_sum.
Your program should return an array containing
two numbers that add up to the target.
"""


def findSum(array, target_sum):
    # Create empty list for output
    twoSum = []
    # Start loop comparing one value to another
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # If values = target sum, add to output list
            if array[i] + array[j] == target_sum:
                twoSum.append(array[i])
                twoSum.append(array[j])
                # Print and return result
                print(twoSum)
                return twoSum
