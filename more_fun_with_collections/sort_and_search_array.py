"""
Program: sort_and_search_array.py
Author: Andy Volesky
Last date modified: 10/20/2021

The purpose of this program:

Write 2 functions sort_array() and search_array().
search_array()
Returns the index of the object in the list or a -1 if the item is not found
sort_array() will sort the list
What is the return statement?
Write a comment explaining why you included return OR
Write a comment explaining why your code has no return statement.

"""
import array as arr

nums = arr.array('i', [5,45,7,9,5,67,87,23,34,56])

def sort_array():
    sort_arr = sorted(nums)
    return sort_arr
# I inlcuded a return because the sorted function creates a copy of the array and must be returned to be useful

def search_array():
    try:
        query = int(input("Input number to search for index: "))
        print(nums.index(query))
        return nums.index(query)
    except ValueError:
        print("-1")
        return "-1"


if __name__ == '__main__':
    search_array()
    sort_array()