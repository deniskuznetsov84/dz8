def my_dict(*args):
    d = {}
    for i in args:
        d.update(i)
    return d

d1 = my_dict({'q': 1, 'w': 2.2})
d2 = my_dict({'e': 3, 'r': 'ups'})

def pal(word):
    return word == word[::-1]

print(pal('шалаш'))