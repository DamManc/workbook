
elements = [
'H', 'He', 'Li', 'Be', 'B',	'C',	'N', 'O',	'F',	'Ne',	'Na',	
'Mg',	'Al',	'Si',	'P',	'S',	'Cl',	'Ar',	
'K',	'Ca',	'Sc', 'Ti',	'V',	'Cr',	'Mn',	'Fe', 'Co',	'Ni',	'Cu',	
'Zn',	'Ga',	'Ge',	'As',	'Se', 'Br',	'Kr',	
'Rb',	'Sr',	'Y',	'Zr',	'Nb',	'Mo',	'Tc',	'Ru',	'Rh', 'Pd',	'Ag',		
'Cd',	'In',	'Sn',	'Sb',	'Te',	'I',	'Xe',	'Cs', 'Ba', 'La',	'Ce',	
'Pr',	'Nd', 'Pm',	'Sm',	'Eu',	'Gd',	'Tb',	
'Dy',	'Ho',	'Er',	'Tm',	'Yb',	'Lu',	'Hf',	'Ta',	'W',	'Re',	'Os',	
'Ir',	'Pt',	'Au',	'Hg',	'Tl',	'Pb',	'Bi',	'Po',	'At',	'Rn',	'Fr',	'Ra',	
'Ac',	'Th',	'Pa',	'U',	'Np',	
'Pu',	'Am',	'Cm',	'Bk',	'Cf',	'Es',	'Fm',	'Md',	'No',	'Lr',	'Rf',	'Db',	
'Sg', 'Bh',	'Hs',	'Mt',	'Ds',	'Rg',	'Cn',	'Nh',	'Fl',	'Mc',	'Lv', 'Ts',	'Og',
]	

def spelling_with_el(input_usr):
    # base case
    if input_usr == '':
        return ''
    # recursive case
    try:
        if len(input_usr) > 1 and (input_usr[0].upper() + input_usr[1].lower()) in elements:
            new_string = input_usr[2:]
            return input_usr[0].upper() + input_usr[1].lower() + spelling_with_el(new_string)
        elif len(input_usr) > 0 and input_usr[0].upper() in elements:
            new_string = input_usr[1:]
            return input_usr[0].upper() + spelling_with_el(new_string)
        else:
            return False
    except TypeError:
        return False
    


def main():
    print('Enter a string:')
    input_usr = input()
    if spelling_with_el(input_usr.strip()):
        print(f'{input_usr} can be spelled as {spelling_with_el(input_usr.strip())}')
    else:
        print(f'{input_usr} can\'t be spelled with chemical elements!')

if __name__ == '__main__':
    main()




