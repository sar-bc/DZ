lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
print(lst)
d = dict()
s = None

for i in lst:
    if type(i) == str:
        d[i] = []
        s = i
    else:
        d[s].append(i)

print(d)
