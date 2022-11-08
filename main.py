def my_dict(*args):
    d = {}
    for i in args:
        d.update(i)
    return d