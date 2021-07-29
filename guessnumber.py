import random

start = input('pleaes choose the maxmum number: ')
start = int(start)
end = input('please choose the minmum number: ')
end = int(end)
ans = random.randint(end, start)
count = 0
while True:
    print('the number start from', end, 'to', start)
    guess = input('Please guess the number: ')
    guess = int(guess)
    count += 1 #count = count + 1
    if ans > guess:
       print('make it bigger')
    elif ans < guess:
       print('make it smaller') 
    else:
       print('You got it in', count, 'times')   

       break