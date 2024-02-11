d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
print(d)
i = 1
q = {}
for k, v in d.items():
    if i < 3:
        q[k] = v
        i += 1
print(q)
