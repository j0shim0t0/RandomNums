from random import *;

def is_valid(n):
    if n.isdigit() == False:
        return False;
    
    if 1 <= int(n) <= 100:
        return True;
    else:
        return False;

rand = randint(1, 100);
countTry = 0;
print('Добро пожаловать в числовую угадайку');

while True:
    print('Введите число от 1 до 100:');
    answer = input();
    
    if is_valid(answer) == False:
        print('А может быть все-таки введем целое число от 1 до 100?');
        continue;
    else:
        answer = int(answer);
    
    countTry += 1;
    
    if answer < rand:
        print('Ваше число меньше загаданного, попробуйте еще разок');
        continue;
    elif answer > rand:
        print('Ваше число больше загаданного, попробуйте еще разок');
        continue;  
    elif answer == rand:
        print('Вы угадали, поздравляем!', 'Количество попыток =', countTry);
        print('Хотите попробовать еще раз? y=да n=нет');
        repeat = input().lower()
        if repeat == 'n':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break;
        else:
            rand = randint(1, 100);
            countTry = 0;            
            continue;
