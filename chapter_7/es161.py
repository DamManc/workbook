import sys


def main():
    if len(sys.argv) != 2:
        print('You must insert the file to read element chemicals')
        quit()
    try:
        fin = open(sys.argv[1], 'r')
        line = fin.readline()
        chemical_elements = []
        while line:
            chemical_elements.append((line.split()[1], line.split()[2]))
            line = fin.readline()
        inp_usr = input('Enter a integer to see the element relate or enter a name o a symbol (blank to finish): ')
        while inp_usr:
            try:
                protons_ele = int(inp_usr)
                if protons_ele <= len(chemical_elements):
                    print(
                        f'{protons_ele} : {chemical_elements[protons_ele][0]}, {chemical_elements[protons_ele][1]}')
                else:
                    print('This value is not correct, enter a new input (leave blank to finish)')
                inp_usr = input()
            except ValueError:
                name_symbol = [el for el in chemical_elements if inp_usr in el]
                if name_symbol:
                    name = ' '.join(name_symbol[0])
                    print(f'{inp_usr}: {name}')
                else:
                    print('This value is not correct, enter a new input (leave blank to finish)')
                inp_usr = input()
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
