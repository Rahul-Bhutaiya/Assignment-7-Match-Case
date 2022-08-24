#Write a python script to display the number of days in a given month number.

month=int(input('Enter any Month Number : '))

match 31 if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 else 2 if month==2 else 30 if month==4 or month==6 or month==9 or month==11 else 'Exit':
    case 31:
        print(month,':',31)
    case 2:
        print(month,':',28,'or',29)
    case 30:
        print(month,':',30)
    case 'Exit':
        print('Enter Valid Input')