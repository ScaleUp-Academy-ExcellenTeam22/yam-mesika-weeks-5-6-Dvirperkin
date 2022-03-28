def join(*args, sep='-'):
    """
    This function get an unlimited number of lists and a character.
    The function return a new list consisting of the contents of all the given lists.
    The contents of all the lists in the new list seperated by the given character.
    """
    if args is ():
        return []

    extended_list_with_separator = []

    for list_to_add in args:
        extended_list_with_separator.extend(list_to_add)
        extended_list_with_separator.append(sep)

    extended_list_with_separator.pop()

    return extended_list_with_separator


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
