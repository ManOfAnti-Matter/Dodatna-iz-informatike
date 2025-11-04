n = int(input())
brojevi = list(map(int, input().split()))
zaokruzeni = list(map(int, input().split()))

zaokruziti = [0] * n

trci = 0
drugi = 2

for i in range(n):
    if brojevi[i] % 2 == 1:
        if not zaokruzeni[i] and (trci or drugi == 2):
            drugi = 0
            zaokruziti[i] = 1
        elif zaokruzeni[i]:
            drugi = 0
        
        trci = 0
    
    else:
        if zaokruzeni[i]:
            trci = 1
        elif trci:
            zaokruziti[i] = 1
    
    if drugi == 0: drugi = 1
    elif drugi == 1: drugi = 2

for z in zaokruziti:
    print(z, end=" ")
