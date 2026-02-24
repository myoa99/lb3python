import math

def arctg_taylor(x, epsilon):
    S = 0
    n = 0
    term = x  # первый член ряда
    while abs(term) >= epsilon:
        S += term
        n += 1
        # вычисляем следующий член ряда: (-1)^(n+1) * x^(2n+1) / (2n+1)
        term = (-1)**(n+1) * (x**(2*n+1)) / (2*n+1)
    return S, n

# Ввод параметров
X_nach = float(input("Введите начальное значение x (Xнач): "))
X_kon = float(input("Введите конечное значение x (Xкон): "))
dx = float(input("Введите шаг dx: "))
epsilon = float(input("Введите точность ε: "))

# Проверка условия |x| ≤ 1
if abs(X_nach) > 1 or abs(X_kon) > 1:
    print("Ошибка: значения x должны удовлетворять условию |x| ≤ 1 для сходимости ряда.")
else:
    # Вывод заголовка и шапки таблицы
    print("\n" + "="*60)
    print("ТАБЛИЦА ЗНАЧЕНИЙ ФУНКЦИИ arctg(x) (РЯД ТЕЙЛОРА)")
    print("="*60)
    print(f"Интервал: [{X_nach}; {X_kon}], шаг: {dx}, точность: {epsilon}")
    print("\n{:>10} {:>20} {:>20} {:>20}".format("x", "arctg(x)", "точное значение", "члены ряда"))
    print("-"*60)

    # Вычисление и вывод значений
    x = X_nach
    while x <= X_kon:
        # Вычисляем приближённое значение и количество членов
        approx_value, num_terms = arctg_taylor(x, epsilon)
        # Вычисляем точное значение для сравнения (функция math.atan)
        exact_value = math.atan(x)
        print(f"{x:>10.4f} {approx_value:>20.10f} {exact_value:>20.10f} {num_terms:>20}")
        x += dx

    print("="*60)
