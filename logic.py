import random

def play_game(min_number, max_number, attempts, initial_capital):
    target_number = random.randint(min_number, max_number)
    capital = initial_capital

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас есть {attempts} попыток, чтобы угадать число от {min_number} до {max_number}.")
    print(f"Ваш начальный капитал: {capital}.")

    for attempt in range(1, attempts + 1):
        try:
            bet = int(input(f"Попытка {attempt}. Введите вашу ставку: "))
            if bet > capital:
                print("У вас недостаточно средств для этой ставки.")
                continue

            guess = int(input(f"Введите ваше число: "))
            if guess < min_number or guess > max_number:
                print(f"Число должно быть в диапазоне от {min_number} до {max_number}.")
                continue

            if guess == target_number:
                capital += bet
                print(f"Поздравляем! Вы угадали число. Ваш капитал теперь: {capital}.")

            else:
                capital -= bet
                print(f"Неверное число. Ваш капитал теперь: {capital}.")

            if capital <= 0:
                print("У вас закончились деньги. Игра окончена.")
                break
        except ValueError:
            print("Пожалуйста, введите допустимое число.")

    if capital > 0 and guess != target_number:
        print(f"Вы исчерпали все попытки. Загаданное число было {target_number}.")

    print("Спасибо за игру!")

