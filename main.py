def my_dict(*args):
    d = {}
    for i in args:
        d.update(i)
    return d

d1 = my_dict({'q': 1, 'w': 2.2})