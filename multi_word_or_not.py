"""
Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""

string_var=input('Enter a String : ')

match 'multiword' if ' ' in string_var else 'singleword':
    case 'multiword':
        print('It\'s Multi-Word String')
    case 'singleword':
        print('It\'s Single-Word String.')