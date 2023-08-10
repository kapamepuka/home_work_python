from random import randint

NUM_ATTEMPTS = 10
target_number = randint(0, 1000)

for attempt in range(NUM_ATTEMPTS):
    guess = int(input(f"Попытка {attempt + 1}/{NUM_ATTEMPTS}: Введите предположение: "))
    
    if guess < target_number:
        print("Больше.")
    elif guess > target_number:
         print("Меньше.")
    else:
        print("Поздравляем! Вы угадали число!")
        break
else:
    print("Попытки закончились. Загаданное число:", target_number)