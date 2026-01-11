n = int(input())

br = 0

for a in range(1, n // 3 + 1):
    for b in range(a, (n - a) // 2 + 1):
        br += 1

print(br)