d, m = map(int, input().split())
mjeseci = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dani = sum(mjeseci[:m - 1]) + d - 1  # - 1 tako da dani pocinju od 0 (bitno za mod operaciju)
if dani == 364:
    print("Dan nove godine")
else:
    print(dani % 28 + 1, dani // 28 + 1)