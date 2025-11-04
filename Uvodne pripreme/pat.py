p = []
m = []

for i in range(4):
    a = int(input())
    p.append(a)

for i in range(4):
    a = int(input())
    m.append(a)

zbroj_p = 0
zbroj_m = 0

for i in range(4):
    zbroj_p += p[i]
    zbroj_m += m[i]

    if zbroj_m < zbroj_p:
        print("PAT")
    else:
        print("MAT")
