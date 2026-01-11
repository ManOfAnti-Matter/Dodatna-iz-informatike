n = input()
d = len(n) // 2

a = int(n[:d])
b = int(n[d:])

print(abs(a - b))