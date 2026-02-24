from math import sqrt

# Ввод параметров
print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

# Вывод параметров
print("Xbeg={0:7.2f} Xend={1:7.2f}".format(xb, xe))
print("Dx={0:7.2f}".format(dx))

# Инициализация начальной точки
xt = xb

# Шапка таблицы
print("+--------+--------+")
print("|    X   |    Y   |")
print("+--------+--------+")

# Цикл по диапазону
while xt <= xe:
    if xt <= -3:
        y = xt + 7  # Линейная часть слева (например, проходит через (-7,0) и (-3,4))
    elif -3 < xt <= -2:
        y = 4
    elif -2 < xt <= 2:
        y = xt**2
    elif 2 < xt <= 4:
        y = -xt+7
    else:
        y = 0

    print("|{0:7.2f} |{1:7.2f} |".format(xt, y))
    xt += dx

# Завершающая линия таблицы
print("+--------+--------+")
