a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
a += ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in a:
    for j in a:
        if i == "z" and j == "z":
            a = a
        print(i + j)
