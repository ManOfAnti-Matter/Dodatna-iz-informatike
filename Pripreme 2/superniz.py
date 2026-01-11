n = int(input())
niz = list(map(int, input().split()))
k = int(input())

najveci = 0

ponavljanja = [0] * 1_000_001
for i in range(n):
    ponavljanja[niz[i]] += 1

    if najveci < niz[i]:
        najveci = niz[i]

superniz = True
najmanji = 0
for x in range(1, najveci + 1):
    if ponavljanja[x] != x:
        superniz = False
        najmanji = x
        break

if superniz:
    print("SUPER")
else:
    print(najmanji)