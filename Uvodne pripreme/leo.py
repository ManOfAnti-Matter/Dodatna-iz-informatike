x = int(input())
l = int(input())
k = int(input())

if abs(k - x) > abs(l - x):
    print(abs(l - x))
else:
    print(abs(k - x))

blizi = 0
if abs(k - x) > abs(l - x):
    blizi = l
elif abs(k - x) < abs(l - x):
    blizi = k
else:
    blizi = l

print(abs(blizi - x) + abs(k - l))

if blizi > x:
    print("G")
else:
    print("D")

