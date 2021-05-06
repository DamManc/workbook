def flattern_list(data):
    if not data:
        return data
    if type(data[0]) == list:
        l1 = flattern_list(data[0])
        l2 = flattern_list([el for el in data if data.index(el) != 0])
        return l1 + l2
    else:
        l1 = [data[0]]
        l2 =  flattern_list([el for el in data if data.index(el) != 0])
        return l1 + l2

def main():
    print('This is a list to flattern')
    data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    print(data)
    print(flattern_list(data))


if __name__ == '__main__':
    main()