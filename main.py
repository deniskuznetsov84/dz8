def my_dict(*args):
    d = {}
    for i in args:
        d.update(i)
    return d

d1 = my_dict({'q': 1, 'w': 2.2})
d2 = my_dict({'e': 3, 'r': 'ups'})
d3 = my_dict({'t': 4, 'y': 0})

print(my_dict(d1, d2, d3))

def pal(word):
    return word == word[::-1]

print(pal('шалаш'))