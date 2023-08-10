def is_prime(number):
    return number > 1 and all(number % i for i in range(2, int(number**0.5) + 1))

try:
    number = int(input("Введите число (от 2 до 100000): "))
    print(f"{number} - {'простое' if is_prime(number) else 'составное'} число.")
except ValueError:
    print("Ошибка ввода. Введите целое число.")
    