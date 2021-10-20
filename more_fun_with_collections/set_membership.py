"""
Program: set_membership.py
Author: Andy Volesky
Last date modified: 10/19/2021

The purpose of this program:

Create a file set_membership.py in more_fun_with_collections.
In set_membership.py
Write a function in_set() that
Accepts a set and a value
Return a boolean value stating if the element is in the set.
Write a main()
Initialize a set called test_set
Initialize a value called test_value
Call in_set() with appropriate values
Print messages as appropriate
The value 'apple' is in the set {'banana', 'apple', 'cherry'}
The value '5' is not in the set {'banana', 'apple', 'cherry'}

"""


def in_set(a_set, a_value):
    """
    Use reST style.
    :param a_set: a set of items
    :param a_value: a value that we want to test in set
    :raise: raises an exception
    :return: return a bool if the value is in set
    """
    if a_value in a_set:
        print(f'The value {a_value} is in the set {a_set}')
    else:
        print(f'The value {a_value} is not in the set {a_set}')


if __name__ == '__main__':
    test_set = {'banana', 'apple', 'cherry'}
    test_value = 'banana'
    in_set(test_set, test_value)
    test_set = {'banana', 'apple', 'cherry'}
    test_value = 10
    in_set(test_set, test_value)
    test_set = {'banana', 'apple', 'cherry'}
    test_value = True
    in_set(test_set, test_value)
    test_set = {'banana', 'apple', 'cherry'}
    test_value = 'cherry'
    in_set(test_set, test_value)
