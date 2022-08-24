"""
Write a python program to check whether a given number is positive, negative or
zero using match case statement
"""

number=int(input('Enter a Number : '))

match 'Positive' if number>0 else 'Negative' if number<0 else 'Zero':
    case 'Positive':
        print('It\'s Positive Number')
    case 'Negative':
        print('It\'s Negative Number')
    case 'Zero':
        print('It\'s Zero')