"""
Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
"""

from unicodedata import category


age=int(input('Enter Your Age : '))

match 'Kid' if -1<age<10 else 'Teen' if 10<=age<20 else 'Young' if 20<=age<40 else 'Experienced' if 40<=age<60 else 'Senior Citizen' if age>=60 else 'Exit':
    case 'Kid':
        print('You are in Kid Category')
    case 'Teen':
        print('You are in Teen Category')
    case 'Young':
        print('You are in Young Category')
    case 'Experienced':
        print('You are in Experienced Category')
    case 'Senior Citizen':
        print('You are in Senior Citizen Category')
    case 'Exit':
        print('Enter Valid Input...')