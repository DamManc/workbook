
name_elements = [
'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron','Carbon','Nitrogen','Oxygen','Fluorine','Neon','Sodium',
'Magnesium','Aluminium','Silicon','Phosphorus','Sulfur','Chlorine','Argon','Potassium','Calcium','Scandium',
'Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt','Nickel','Copper','Zinc','Gallium'	,'Germanium',
'Arsenic','Selenium','Bromine','Krypton','Rubidium','Strontium','Yttrium','Zirconium','Niobium','Molybdenum',
'Technetium','Ruthenium','Rhodium','Palladium','Silver','Cadmium','Indium','Tin','Antimony','Tellurium','Iodine',
'Xenon','Caesium','Barium','Lanthanum','Cerium','Praseodymium','Neodymium','Promethium','Samarium','Europium',
'Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium','Hafnium','Tantalum','Tungsten',
'Rhenium','Osmium','Iridium','Platinum','Gold','Mercury','Thallium','Lea','Bismuth','Polonium','Astatine','Radon',
'Francium','Radium','Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium',
'Berkelium','Californium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium','Dubnium',
'Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadtium','Roentgenium','Copernicium','Nihonium','Flerovium',
'Moscovium','Livermorium','Tennessine','Oganesson',
]	


def elements_seq(n_element):
    res = [el for el in name_elements if el.startswith(n_element[-1].upper())]
    if len(res) > 0:
        element = res[0]
        name_elements.remove(element)
        new_n_element = element
        return element + '\t' + elements_seq(new_n_element)
    else:
        return ''

def main():
    print('Enter a name of chemical element:')
    n_element = input()
    while n_element not in name_elements:
        print('Your value entered is not correct..')
        print('Enter a name of chemical element:')
        n_element = input()
    print('Start the game...')
    print(elements_seq(n_element))



if __name__ == '__main__':
    main()