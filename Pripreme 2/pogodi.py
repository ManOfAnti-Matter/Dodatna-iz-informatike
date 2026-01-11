n = int(input())
a = list(map(int, input().split()))
d = list(map(int, input().split()))

for x in range(250, 0, -1):
    razlike = []
    for broj in a:
        razlike.append(abs(x - broj))
    razlike.sort()
    if razlike == d:
        print(x)
        break