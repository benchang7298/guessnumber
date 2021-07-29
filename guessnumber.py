import random
ans = random.randint(1, 100)

while True:
    guess = input('Please guess the number from 1 to 100: ')
    guess = int(guess)
    if ans > guess:
       print('make it bigger')
    elif ans < guess:
       print('make it smaller') 
    else:
       print('You got it')        
       break