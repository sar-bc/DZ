d = {'one': 'first'}
print(d)


def db(**kwargs):
    d.update(**kwargs)


db(k1=22, k2=31, k4=91)
print(d)
