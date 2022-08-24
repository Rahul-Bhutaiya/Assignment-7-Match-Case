"""
Write a python script to check whether a given year is
a. Non century leap year ex:2020
b. Century leap year ex:2000
c. Non century non leap year ex:2021
d. Century non leap year ex:1900
"""

year=int(input('Enter a Year : '))

match 'Century leap year' if year%400==0 else 'Century non leap year' if year%100==0 else 'Non century leap year' if year%4==0 else 'Non century non leap year':
    case 'Century leap year':
        print('It\'s Century Leap Year')
    case 'Century non leap year':
        print('It\'s Century Year, But Not a Leap Year')
    case 'Non century leap year':
        print('It\'s Not Century Year, But It\'s a Leap Year')
    case 'Non century non leap year':
        print('It\'s Not Century and Not Leap Year')