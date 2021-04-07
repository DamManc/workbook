#Exercise 134:Generate All Sublists of a List

def sublists(my_list):
    sublists = []
    for token in my_list:
        sublists.append(list(token))
    for i in range(0, len(my_list) - 1):
        n = list(my_list[i])
        n.append(my_list[i+1])
        sublists.append(n)
    sublists.append([])
    sublists.append(my_list)
    return sublists


def main():
    my_list = []
    print('Enter an string to create a list (blank to finish)')
    l = input()
    while l:
        my_list.append(l)
        l = input()
    print(f'All Sublists {sublists(my_list)}')


if __name__ == '__main__':
    main()