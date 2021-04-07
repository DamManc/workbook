# Exercise 133:Does a List Contain a Sublist?

def is_sublist(larger, smaller):
    index_list = []
    for token in smaller:
        try:
            i = larger.index(token)
            index_list.append(i)
        except ValueError:
            return False
    for i in range(0, len(index_list) - 1):
        if index_list[i] == (index_list[i+1] - 1):
            value = 1
        else:
            value = 0
    if value == 1:
        return True
    else:
        return False


def main():
    larger = []
    smaller = []
    print('Enter an integer to create a list (blank to finish)')
    l = input()
    while l:
        larger.append(l)
        l = input()
    print('Enter an integer to create another list (blank to finish)')
    m = input()
    while m:
        smaller.append(m)
        m = input()
    if is_sublist(larger, smaller):
        print('Your second list is a Sublist of the first one!!')
    else:
        print('Your second list is not a Sublist to the first one..')


if __name__ == '__main__':
    main()
