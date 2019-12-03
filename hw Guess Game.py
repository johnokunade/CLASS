from random import randint
from time import sleep
print(''' Welcome to guess my number game Pick a number from 1 to 50 Enjoy!!!
''')
print("Thinking...")
sleep(2)
print("3...")
sleep(2)
print("2...")
sleep(2)
print("1...")

a = 1
compno = randint (1, 50)
guess = int(input ('Pick a number from 1 to 50:'))
while guess != compno:
    if guess > compno:
        print('guess lower...')
    
    else:
        print('guess higher...')
    guess = int(input('pick a number from 1 to 50: '))
    a = a+1
    if a == 4:
        print('You have 1 trial left')
    if a == 5:
        break

if guess == compno:
    print('Correct! you guessed right')
    print(f'you tried it {a} times')

else:
    print(' Sorry, you didin\'t guess right after 5 trials ')
    print (f'The number is {compno}')
