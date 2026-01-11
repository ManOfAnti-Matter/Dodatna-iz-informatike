n = int(input())
m = []
t = []
for i in range(n):
    m1, t1 = map(int, input().split())
    m.append(m1)
    t.append(t1)
x = int(input())

suma = m[0] * t[0]
for i in range(n - 1):
    razlika = m[i + 1] - m[i] - 1

    gornji = razlika // 2
    donji = razlika - gornji

    if m[i] < x <= m[i] + donji:
        print(t[i])
    if m[i + 1] - gornji <= x <= m[i + 1]:
        print(t[i + 1])

    suma += donji * t[i] + (gornji + 1) * t[i + 1]
suma += (1440 - m[n - 1]) * t[n - 1]

if x <=   m[0]:
    print(t[0])
if x > m[n - 1]:
    print(t[n - 1])

print(suma)