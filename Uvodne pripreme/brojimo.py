a = int(input())
b = int(input())
c = int(input())

if b == 1:
    x = c - b
else:
    x = b - a

if c + x > 100:
    print(1)
else:
    print(c + x)