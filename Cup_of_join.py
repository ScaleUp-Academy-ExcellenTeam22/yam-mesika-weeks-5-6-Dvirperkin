def join(*args, sep='-'):
    if args is None:
        return []

    new_list = []

    for lst in args:
        new_list.extend(lst)
        new_list.append(sep)

    new_list.pop()

    return new_list


print(join([1, 2], [8], [9, 5, 6], sep='@'))
