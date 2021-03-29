# Exercise 114: Negatives,Zeros and Positives

def main():
    n = input('Enter integers N, where N can be -N, 0, +N (blank line to finish and move forward): ')
    pos_n = []
    neg_n = []
    while n != '':
        try:
            int_n = int(n)
            if int_n >= 0:
                pos_n.append(int_n)
            else:
                neg_n.append(int_n)
            n = input('Enter integers N, where N can be -N, 0, +N (blank line to finish and move forward): ')
        except ValueError:
            print('Enter a valid value: ')
            n = input('Enter integers N, where N can be -N, 0, +N (blank line to finish and move forward): ')
    print('All of the negative numbers, followed by all of the zeros, followed by all of the positive numbers')
    for i in sorted(neg_n):
        print(i, end=' ')
    for i in sorted(pos_n):
        print(i, end=' ')


if __name__ == '__main__':
    main()
