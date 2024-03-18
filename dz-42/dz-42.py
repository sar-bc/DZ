import os

lst = []
for k in os.listdir("files"):
    lst.append(fr"files\{k}")

print(sorted(lst, reverse=True))
print("*" *20)
root = "files"
objs = os.listdir(root)
print(objs)
objs = list(map(lambda i: os.path.join(root, i), objs))
print(objs)
objs_sort = sorted(objs, key=os.path.isfile, reverse=True)
print(objs_sort)
