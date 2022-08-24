#Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

print('Enter...\n1 : Addition\n2 : Subtraction\n3 : Multiplication\n4 : Division')


match int(input('\nWhat You Want to Do....: ')):
    case 1:
        print('Addition : ',int(input('Enter First Value : '))+int(input('Enter Second Value : ')))
    case 2:
        print('Subtraction : ',int(input('Enter First Value : '))-int(input('Enter Second Value : ')))
    case 3:
        print('Multication : ',int(input('Enter First Value : '))*int(input('Enter Second Value : ')))
    case 4:
        print('Division : ',int(input('Enter First Value : '))/int(input('Enter Second Value : ')))
    case _:
        print('Enter a Valid Input.')