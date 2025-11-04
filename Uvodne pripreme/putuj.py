s = int(input())
m = int(input())
x = int(input())

if s * 60 + m > 7 * 60 + 30:
    vrijeme = x + m - 30  # = x + (s * 60 + m - 7 * 60 - 30)  { s <= 7 pa mora biti s == 7 }
elif s * 60 + m < 7 * 60:
    vrijeme = x + m - 60  # = x - (s * 60 + m - 7 * 60)  { s >= 6 pa mora biti s == 6 }
else:
    vrijeme = x

minute = s * 60 + m + vrijeme

print(vrijeme)
print(minute // 60, minute % 60)