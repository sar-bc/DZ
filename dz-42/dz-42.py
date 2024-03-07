import os

# print(os.listdir("files"))
for root, dirs, files in os.walk("files"):
    print(root)