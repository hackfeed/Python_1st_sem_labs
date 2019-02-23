""" Вычисление суммы бесконечного ряда с точностью Epsilon.

Данная программа вычисляют сумму бесконечного ряда, общий член которого
задан формулой a_n = (-1)^n * ((Pi/3)^(2n+1)/(2n+1)!)
На старте программы задаются значения начального показываемого значения
n, при котором показывается сумма, шаг для вывода, максимальное
количество шагов, и точность Epsilon. Если за максимальное количество
шагов ряд не сошёлся, то выводится соответствующее сообщение.

Входные данные:

n_show - номер члена, с которого начинается вывод суммы
n_step - шаг для каждого последующего вывода
n_max - максимальное количество шагов
eps - точность для a_n члена

Выходные данные:

k - количество просумированных членов на данный момент
sum_an - сумма ряда при k членах

Пример входных данных:

Введите число, с которого начать показ суммы: 5
Введите шаг с которым показывать сумму: 2
Введите максимальное количество шагов: 60
Введите точность (eps): 1e-20

Пример выходных данных:

***********************
  n  |   Current sum
***********************
  5  |     0.86602
***********************
  7  |     0.86602
***********************
  9  |     0.86602
***********************
 11  |     0.86602
***********************
Ряд сошёлся за 11 шагов

"""

from math import factorial, pi

n_show = int(input("Введите число, с которого начать показ суммы: "))
n_step = int(input("Введите шаг с которым показывать сумму: "))
n_max = int(input("Введите максимальное количество шагов: "))
eps = float(input("Введите точность (eps): "))

if n_show < 1 or n_step < 1 or n_max < 1:
    print("Введены некорректные значения, проверьте правильность ввода!")
else:
    a_n = round(pi/3, 5)
    sum_an = a_n
    k = 1

    print("*"*23)
    print("{0:^5s}|{1:^17s}".format("n", "Current sum"))
    print("*"*23)

    while abs(a_n) > eps and k <= n_max:
        if k % n_show == 0:
            print("{0:^5d}|{1:^17.5f}".format(k, sum_an))
            print("*"*23)
            n_show += n_step
        a_n = (-1)**k * ((pi/3)**(2*k + 1)/factorial(2*k + 1))
        sum_an += round(a_n, 5)
        k += 1

    if k > n_max:
        print("Ряд не сошёлся за %d шагов" % n_max)
    else:
        print("Ряд сошёлся за %d шагов" % (k-1))