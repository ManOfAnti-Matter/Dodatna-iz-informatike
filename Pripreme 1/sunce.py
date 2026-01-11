d = input()
formati = ["2d2m4g", "2d4g2m", "2m2d4g", "2m4g2d", "4g2m2d", "4g2d2m"]
mjeseci = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
datumi = []

for f in formati:
    index = 0
    datum = [0, 0, 0]
    for i in range(3):
        broj = int(f[2*i])
        znak = f[2*i + 1]
        
        n = int(d[index:index + broj])
        if znak == "d": datum[0] = n
        elif znak == "m": datum[1] = n
        else: datum[2] = n
        index += broj
    
    if not datum in datumi:
        datumi.append(datum)

for datum in datumi:
    [dan, mjesec, godina] = datum
    if not 1 <= mjesec <= 12:
        continue
    
    if mjesec == 2 and (godina % 4 == 0 and godina % 100 != 0 or godina % 400 == 0):
        granica = 29
    else:
        granica = mjeseci[mjesec - 1]
    
    if not 1 <= dan <= granica:
        continue
    
    if datum[::-1] <= [2016, 3, 17]:
        continue

    print(dan, mjesec, godina, sep=".", end="")
    print(".")
    