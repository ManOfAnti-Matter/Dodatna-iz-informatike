n = int(input())
t = []
for i in range(n):
    t.append(int(input()))
k = int(input())
x = []
for i in range(k):
    x.append(int(input()))

najdesniji = 0
polica = [0] * 501
for i in range(n):
    if najdesniji < t[i]:
        najdesniji = t[i]
    polica[t[i]] = i + 1


for zamjena in range(k):
    i_lijevi = najdesniji - x[zamjena]
    i_desni = najdesniji

    najdesniji = 0

    uzastopni = 0
    pocetak = i_lijevi
    kraj = pocetak - 1
    while uzastopni < x[zamjena] + 1:
        pocetak -= 1
        uzastopni += 1

        if polica[pocetak] != 0:
            uzastopni = 0
            if najdesniji == 0:
                najdesniji = pocetak
            kraj = pocetak - 1
    
    if najdesniji == 0:
        najdesniji = kraj

    polica = polica[:pocetak] + polica[i_lijevi:i_desni + 1] + polica[kraj + 1: i_lijevi] + polica[pocetak:kraj + 1] + polica[i_desni + 1:]

for b in polica:
    if b != 0:
        print(b)
