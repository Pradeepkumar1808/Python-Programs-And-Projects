import random
from random import randrange

n=randrange(1,100)

guess=int(input('Please Enter The Number: '))
while n!=guess:

    if guess<n:
        print('Too Low!!!\n')
        guess=int(input('Enter Number Again! \n'))

    elif guess>n:
        print('Too High!!!\n')
        guess = int(input('Enter Number Again! \n'))

    else:
        break

print("You guessed it right!!!! Hurray!!!!")
