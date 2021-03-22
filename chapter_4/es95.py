# Exercise 95: Capitalize It


def correct_cap(s):
    s_n = s.strip().lower().capitalize()  # DEL WHITESPACES, ALL CH IN LOWERCASE AND CAPITALIZE THE INIT CH
    for i in range(1, len(s_n)):
        if s_n[i] == 'i' and s_n[i - 1].isspace() and (
                s_n[i + 1] == "'" or s_n[i + 1] == '?' or s_n[i + 1] == '!' or s_n[i + 1].isspace()):
            s_n = s_n[:i] + s_n[i].upper() + s_n[i+1:]
    for i in range(2, len(s_n)+1):
        if (s_n[i-2] == '.' or s_n[i - 2] == '?' or s_n[i - 2] == '!') and s_n[i-1].isspace():
            s_n = s_n[:i] + s_n[i].upper() + s_n[i+1:]
    return s_n


def main():
    input_string = input('Enter a string: ')
    print(correct_cap(input_string))


if __name__ == '__main__':
    main()
