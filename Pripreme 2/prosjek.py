n = int(input())
b = list(map(int, input().split()))

print(b[0], end=" ")
for i in range(1, n):
    print((i + 1) * b[i] - i * b[i - 1], end=" ")