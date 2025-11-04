n = int(input())
t = 0
m = 0
trenutak = 0

for i in range(n):
    glas = input()
    if glas == "T":
        t += 1
    else:
        m += 1
    
    if (2 * t > n or 2 * m > n) and trenutak == 0:
        trenutak = i + 1
    
print(max(t, m))
print(trenutak)
    