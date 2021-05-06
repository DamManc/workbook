def run_length_dec(li):
    if len(li) > 1:
        new_li = li[2:]
        return [li[0] for n in range(li[1])] + run_length_dec(new_li)
    else:
        return []    
    
def main():
    print('Your compressed list is:')
    compr_li = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(compr_li)
    print(f'Your decompressed lis is {run_length_dec(compr_li)}')


if __name__ == '__main__':
    main()