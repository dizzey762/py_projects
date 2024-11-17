from math import *
import random

random_num = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')

#Проверка числа
def is_valid(user_num):
    return user_num.isdigit() and 1 <= int(user_num) <= 100

#Проверка числа введенного пользователем
def is_valid_num():
    while True:
        print('Введите число от 1 до 100:')
        n = input()
        if(is_valid(n)):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
        



# Новая игра

def new_game():
    print('Хотите продолжить игру? (да/нет?)')
    ans = input()
    while True:
        if(ans.lower() == 'да'):
            return True
        else:
            return False



#Игра    

def compare_num():
    count = 0
    while True:
        s = is_valid_num()
        if s < random_num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > random_num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали. поздравляем!')
            
            count += 1
            print(f'Количество попыток: {count}')
            if new_game():
                continue
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
            

compare_num()



        


