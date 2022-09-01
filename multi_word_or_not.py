"""
Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""

string_var=input('Enter a String : ')

match string_var:
    case string_var if ' ' in string_var.strip(): #YOU CAN USE IF STATEMENT WITH CASE ALSO
        print('It\'s Multi-Word String')
    case string_var if ' ' not in string_var.strip():
        print('It\'s Single-Word String.')
