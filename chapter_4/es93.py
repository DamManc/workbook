# Center a String in the TerminalWindow
import shutil

v_str = input('Enter a string: ')
w_terminal = shutil.get_terminal_size()[0]


def center_string(s, w):
    if len(s) >= w:
        return s
    else:
        n_spaces = (w - len(s)) // 2
        new_string = f"{n_spaces * ' '}{s}"
        return new_string


def main():
    for i in range(0, 5):
        string = center_string(v_str, w_terminal)
        print(string)


if __name__ == '__main__':
    main()
