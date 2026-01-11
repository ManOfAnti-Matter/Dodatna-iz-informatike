n, k, m = map(int, input().split())
brojevi = [0]
for i in range(n):
    brojevi.append(int(input()))

suprotni = [0] * (n + 1)
for i in range(1, n + 1):
    if suprotni[brojevi[i]] == 0:
        suprotni[brojevi[i]] = [i]
    else:
        suprotni[brojevi[i]].append(i)

trenutni = [m]
for i in range(k - 1):
    novi = []
    for t in trenutni:
        if suprotni[t] != 0:
            novi += suprotni[t]
    trenutni = novi

trenutni.sort()
for t in trenutni:
    print(t)