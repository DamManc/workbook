# Exercise 124: Line of Best Fit


def calc_best(points):
    per_x_y = 0
    sum_x = 0
    sum_y = 0
    n = len(points)
    sum_x_x = 0
    for point in points:
        per_x_y += point[0] * point[1]
        sum_x += point[0]
        sum_y += point[1]
        sum_x_x += point[0] * point[0]
    avg_x = sum_x / n
    avg_y = sum_y / n
    m = (per_x_y - ((sum_x * sum_y) / n)) / (sum_x_x - (((sum_x) ** 2) / n))
    b = avg_y - m * avg_x

    return m, b


def main():
    i_x = input('Enter a x coordinate (blank to finish): ')
    points = []
    while i_x != '':
        n = 1
        point = []
        try:
            x = float(i_x)
            point.append(x)
            i_y = input('Enter a y coordinate: ')
            while n != 0:
                try:
                    y = float(i_y)
                    n = 0
                    point.append(y)
                    points.append(point)
                except ValueError:
                    print('Error with y coordinate..')
                    i_y = input('Enter a y coordinate: ')
            i_x = input('Enter a x coordinate (blank to finish): ')
        except ValueError:
            print('your input is not a number...')
            i = input('Enter a x coordinate (blank to finish): ')
    print('Your line for the best fit is:')
    print(f'y = {round(calc_best(points)[0], 2)}x + {round(calc_best(points)[1], 2)}')


if __name__ == '__main__':
    main()
