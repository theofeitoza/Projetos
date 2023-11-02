from random import randint
comput=randint(1,10)

print('='*30)
print('  Guess The Number (1 to 10)')
print('='*30)
while True:
    num=int(input('Type the number: '))
    if num < comput:
        print('Guess again. Too low.')
        print('-'*30)
    elif num > comput:
        print('Guess again. Too high.')
        print('-'*30)   
    if num == comput:
        print('Congratulations!!! You won.')
        break