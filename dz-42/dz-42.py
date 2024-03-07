import os

lst = []
for k in os.listdir("files"):
    lst.append(fr"files\{k}")

print(sorted(lst, reverse=True))


