s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s = i
        s = i + s
        print(s)