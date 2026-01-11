p = int(input())
k = int(input())

i = (p - k) // 20

if 20 * i > p - k - 10:
    print(k + 10 * i)
else:
    print(p - 10 * (i + 1))