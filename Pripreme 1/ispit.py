p = int(input())
t = int(input())
n = int(input())
m = int(input())
x = list(map(int, input().split()))

moguci = []
for i in range(p + 1):
    for j in range(p - i + 1):
        if t * i - n * j < 0:
            break
        moguci.append(t * i - n * j)

maksimum = 0
br = 0
for e in x:
    if e in moguci:
        if maksimum < e:
            maksimum = e
    else:
        br += 1

print(br)
print(maksimum)
