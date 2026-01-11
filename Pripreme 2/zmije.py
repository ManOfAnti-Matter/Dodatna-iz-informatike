n = int(input())
kavezi = [0]
for i in range(n):
    kavezi.append(int(input()))

def sljedeca_boja(boja):
    if boja == 'A': return 'B'
    elif boja == 'B': return 'C'
    else: return'A'

svjetla = [0] * (n + 1)
i = 1
boja = 'A'
while i <= n:
    if svjetla[i]:
        i += 1
        continue

    pocetak = i

    while True:
        if svjetla[kavezi[i]] == boja:
            svjetla[kavezi[i]], svjetla[kavezi[kavezi[i]]] = svjetla[kavezi[kavezi[i]]], svjetla[kavezi[i]]
        svjetla[i] = boja

        i = kavezi[i]
        
        boja = sljedeca_boja(boja)

        if pocetak == i:
            break;

for i in range(1, n + 1):
    print(svjetla[i], end='')