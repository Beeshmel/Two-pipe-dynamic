import math

import numpy as np
import matplotlib.pyplot as plt

# теплообменник труба в трубе
L = 60  # м, длина трубки
r1 = 0.1  # м, радиус трубки
r2 = 0.15  # м, радиус наружной трубки
n = 100  # количество используемых узлов

m1 = 3  # кг/с массовый расход
Cp1 = 4180  # Дж/кг К удельная теплоемкость вещества (вода)
density1 = 1000  # кг/м3 плотность вещества (вода)

m2 = 5  # кг/с массовый расход
Cp2 = 4180  # Дж/кг К удельная теплоемкость вещества (вода)
density2 = 1000  # кг/м3 плотность вещества (вода)

pi = 3.1415
S1 = math.pi * r1 ** 2  # м2 площадь проходного сечения
S2 = math.pi * r2 ** 2 - S1

Tin1 = 400  # К температура на входе 1-го потока
Tin2 = 800  # К температура на входе 2-го потока
T0 = 300

U = 340  # коэфициент теплоотдачи

dx = L / n
t_final = 1000  # с, время моделирования
dt = 1  # с, шаг времени

x = np.linspace(dx / 2 , L - dx / 2 , n)

T1 = np.ones(n) * T0
T2 = np.ones(n) * T0

dT1dt = np.zeros(n)
dT2dt = np.zeros(n)

t = np.arange(0 , t_final , dt)

for j in range(1 , len(t)):
    plt.clf()

    dT1dt[1:n] = (m1 * Cp1 * (T1[0:n - 1] - T1[1:n]) + U * 2 * math.pi * r1 * dx * (T2[1:n] - T1[1:n])) / (density1 * Cp1 * dx * S1)
    dT1dt[0] = (m1 * Cp1 * (Tin1 - T1[0]) + U * 2 * math.pi * r1 * dx * (T2[0] - T1[0])) / (density1 * Cp1 * dx * S1)

    dT2dt[1:n] = (m2 * Cp2 * (T2[0:n - 1] - T2[1:n]) - U * 2 * math.pi * r1 * dx * (T2[1:n] - T1[1:n])) / ( density2 * Cp2 * dx * S2)
    dT2dt[0] = (m2 * Cp2 * (Tin2 - T2[0]) - U * 2 * math.pi * r1 * dx * (T2[0] - T1[0])) / ( density2 * Cp2 * dx * S2)

    T1 = T1 + dT1dt*dt
    T2 = T2 + dT2dt*dt

    plt.figure(1)
    plt.plot(x,T1, color = "blue", label = "Внутри")
    plt.plot(x,T2, color = "red", label = "Снаружи")

    plt.axes([0,L,298,820])
    plt.xlabel("Расстояние в метрах")
    plt.ylabel("Температура (К)")

    plt.draw()
    plt.pause(0.05)



