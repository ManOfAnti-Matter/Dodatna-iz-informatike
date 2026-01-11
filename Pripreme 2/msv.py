n = int(input())
b = []
for i in range(n):
    b.append(int(input()))

msv = [0, 0, 0]
index = 0

for broj in b:
    msv[index] += broj
    if broj != 6:
        index = (index + 1) % 3

print(sum(msv))
print(msv[0], msv[1], msv[2])