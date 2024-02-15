t = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# print(list(filter(lambda x: x == x[::-1], t)))
print(list(map(lambda x: x, filter(lambda x: x == x[::-1], t))))

