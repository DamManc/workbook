
def edit_distance(s_1, s_2):
    if len(s_1) == 0:
        return len(s_2)
    elif len(s_2) == 0:
        return len(s_1)
    else:
        cost = 0
        if s_1[-1] != s_2[-1]:
            cost = 1 
        d1 = edit_distance(s_1[:-1], s_2) + 1
        d2 = edit_distance(s_1, s_2[:-1]) + 1
        d3 = edit_distance(s_1[:-1], s_2[:-1]) + cost
        return min(d1, d2, d3)


def main():
    print('Insert a string')
    s_1 = input()
    print('Insert a second string')
    s_2 = input()
    print(f'The edit distance is: {edit_distance(s_1, s_2)}')

if __name__ == '__main__':
    main()