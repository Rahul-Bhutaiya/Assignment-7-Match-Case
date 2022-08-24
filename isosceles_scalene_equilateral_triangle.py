"""
Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
    b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
    c. Check whether a given set of three numbers are equilateral triangle or not
    d. Exit.
"""

first_num,second_num,third_num=int(input('Enter First Number : ')),int(input('Enter Second Number : ')),int(input('Enter Third Number : '))

match 'Equilateral Triangle' if first_num==second_num==third_num else 'Isosceles Triangle' if first_num==second_num or first_num==third_num or second_num==third_num else 'Scalene Triangle':
    case 'Equilateral Triangle':
        print('It\'s Equilateral Triangle')
    case 'Isosceles Triangle':
        print('It\'s Isosceles Triangle')
    case 'Scalene Triangle':
        print('It\'s Scalene Triangle')