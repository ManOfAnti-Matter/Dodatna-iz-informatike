n = int(input())
x = int(input())
a = []
for i in range(n - 1):
    a.append(int(input()))

br = 0
while x != n:
    x = a[x - 1]
    br += 1

print(br)