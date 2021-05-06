
def run_length_comp(l):
    max = len(l)
    if l:
        n = 0
        ch = l[0]
        while ch == l[0]:
            n += 1
            if n < max:
                ch = l[n]
            else:
                ch = []
        new_li = [l[0], n]
        return new_li + run_length_comp(l[n:])
    else:
        return []

def main():
    print('Enter a string to compress')
    list_in = list(input())
    print(run_length_comp(list_in))


if __name__ == '__main__':
    main()