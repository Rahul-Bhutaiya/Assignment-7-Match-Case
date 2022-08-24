"""
Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
"""

str_1=input('Enter First String : ')
str_2=input('Enter Second String : ')

match 'same' if str_1==str_2 else 'str_1' if str_1>str_2 else 'str_2':
    case 'same':
        print('Both Strings are Identical')
    case 'str_1':
        print('First String Comes After The Second String In Dictionary Order')
    case 'str_2':
        print('First String Comes Before The Second String In Dictionary Order')