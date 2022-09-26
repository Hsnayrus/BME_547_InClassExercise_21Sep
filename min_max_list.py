def min_max_list(list):
    minimum_value = min(list)
    maximum_value = max(list)
    return minimum_value, maximum_value


if __name__ == '__main__':
    min_val, max_val = min_max_list([1, 2, 3, 4, 5])
    print(min_val, max_val)
