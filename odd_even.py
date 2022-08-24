"""
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.

"""

number=int(input('Enter a Number : '))

match 'Saurabh Shukla' if number%2==0 else 'Prateek Jain' if number<0 and number%2 else 'Aditya Choudhary':
    case 'Saurabh Shukla':
        print('Saurabh Shukla')
    case 'Prateek Jain':
        print('Prateek Jain')
    case 'Aditya Choudhary':
        print('Aditya Choudhary')