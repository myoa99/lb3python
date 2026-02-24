from math import *
from random import uniform

print(" X Y Res")
print("-------------------")

for n in range(10):
    x = uniform(-9, 7)  # Диапазон x по графику
    y = uniform(0, 10) # Диапазон y с запасом
    flag = 0

    if -7 <= x <= 4:  # Проверяем, что x в пределах графика
        if x <= -3:
            if y <= x + 7:
                flag = 1
        elif -3 < x < 3:
            if y <= x**2 - 1:
                flag = 1
        elif x >= 3:
            if y <= -x + 7:
                flag = 1

    print("{0:7.2f} {1:7.2f}".format(x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")
