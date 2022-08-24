"""
Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
"""

ask=input('Hey.! Which is Your Favourite Color...? : ')

match 'red' if 'red' in ask else 'yellow' if 'yellow' in ask else 'blue' if 'blue' in ask else 'orange' if 'orange' in ask else 'white' if 'white' in ask else 'black' if 'black' in ask else 'sunday':
    case 'yellow':
        print('Monday')
    case 'blue':
        print('Tuesday')
    case 'orange':
        print('Wednesday')
    case 'white':
        print('Thursday')
    case 'black':
        print('Friday')
    case 'red':
        print('Saturday')
    case 'sunday':
        print('Sunday')
