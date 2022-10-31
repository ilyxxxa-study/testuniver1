'''проверочный код из методических материалов
sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

if s > smax:
    smax = s

print("Максимальная площадь треугольника", smax)'''

#домашнее задание ax^2+bx+c=0 дискриминант(D^2-4ac (if D=0 --> D=b/2a)) , теорема виета (x1*x2 = c; x1+x2=-b)
import math
 
print("введите коэффициенты для уравнения ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x1 = float(0)
x2 = float(0)
 
d = b**2-4*a*c
print("дискриминант = ", d)
 
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("x1 = ", x1, "x2 = ", x2)
elif d == 0:
    x = -b/(2*a)
    print("x = ", x)
else:
    print("нет корней")

