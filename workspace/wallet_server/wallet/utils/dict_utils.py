import collections


def sorted_dict_by_key(unsorted_dic: dict):
    return collections.OrderedDict(
        sorted(unsorted_dic.items(), key=lambda keys: keys[0])
    )