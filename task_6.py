# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random


def guess_number(secret_number, attempts):
    if attempts == 0:
        print(f"Вы проиграли! Было загадано число {secret_number}")
        return

    user_number = int(input("Введите число от 0 до 100: "))

    if user_number == secret_number:
        print("Вы угадали!")
        return
    elif user_number > secret_number:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")

    guess_number(secret_number, attempts - 1)


secret_number = random.randint(0, 100)

guess_number(secret_number, 10)
