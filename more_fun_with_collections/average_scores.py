"""
Program: average_scores.py
Author: Andy Volesky
Last date modified: 10/19/2021

The purpose of this program:

Write a program that prompts the user for test scores, stores them in a dictionary, and averages the scores.
Write a function get_test_scores()
Create an empty dictionary scores_dict = dict()
Prompt the user to input the number of test scores, store in num_scores
Write a loop to get each of the num_scores test scores
Prompt the user to input each test score and store in score. (Validate the input!)
Add score to scores_dict  # HINT: update the dictionary
Write a second function average_scores() that accepts the dictionary as the only parameter and returns the average scores
Use len() to determine your num_scores for calculation
Note a dictionary is a set of key, value pairs.
You can get the keys with .keys() function
You can access the value using a key variable scores_dict.get(k)
What about testing?
Write a main to test your functions
Unit Tests can also help test average_scores()

"""


def get_test_scores():
    """
    Use reST style.
    :return: return a dictionary of test scores
    """
    scores_dict = dict()
    num_scores = int(input("Input Number of Scores: "))
    for x in range(0, num_scores):
        score = int(input("Input Score: "))
        try:
            if 0 <= score <= 100:
                scores_dict.update({f'Test {x+1}': score})
            elif score < 0 or score > 100:
                print("Invalid Test Score Entry")
        except:
            print('Valid Number Please')
    print(scores_dict)
    return scores_dict


def average_scores(scores_dict):
    """
    Use reST style.
    :param scores_dict: a dictionary of test scores
    :return: return average of all test scores
    """
    try:
        num_scores = len(scores_dict)
        total = 0
        for x in scores_dict:
            total = total + scores_dict.get(x)
        average = total/num_scores
        print(average)
    except ZeroDivisionError:
        raise ZeroDivisionError("Exception!")
    return average

if __name__ == '__main__':
    scores_dict = get_test_scores()
    average_scores(scores_dict)
