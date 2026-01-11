n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())

x = min(a, b)
y = max(a, b)

print(sum(d[x - 1:y - 1]))