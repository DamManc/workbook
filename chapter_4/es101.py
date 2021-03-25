# Exercise 101: Random License Plate
import random
import string


def gen_plate(plate):
    v_plate = ''
    if plate == 'New':
        for i in range(0, 8):
            if i < 4:
                v_plate += string.digits[random.randint(0, 9)]
            else:
                v_plate += string.ascii_letters[
                    random.randint(0, 52)]  # latin alphabet (lower and uppercase)
    else:
        for i in range(0, 7):
            if i < 3:
                v_plate += string.ascii_letters[random.randint(0, 52)]
            else:
                v_plate += string.digits[random.randint(0, 9)]
    return v_plate


def main():
    r_type = random.random()
    if r_type > 0.5:
        p_type = 'New'
    else:
        p_type = 'Old'
    p_value = gen_plate(p_type)
    print(f'Random licence plate: type: {p_type}, value: {p_value}')


if __name__ == '__main__':
    main()
