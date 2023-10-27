def factorial(n):

    if n < 0:
        return "Факторіал визначений лише для невід'ємних цілих чисел."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
print(f"Факторіал числа {n} дорівнює {factorial(n)}")
