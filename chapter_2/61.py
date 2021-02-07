# Is a License Plate Valid?
license_plate = str(input("Enter a license plate: "))
if (
    len(license_plate) == 6
    and license_plate[0] >= "A"
    and license_plate[0] <= "Z"
    and license_plate[1] >= "A"
    and license_plate[1] <= "Z"
    and license_plate[2] >= "A"
    and license_plate[2] <= "Z"
    and license_plate[3] >= "0"
    and license_plate[3] <= "9"
    and license_plate[4] >= "0"
    and license_plate[4] <= "9"
    and license_plate[5] >= "0"
    and license_plate[5] <= "9"
):
    print("The plate is valid older style plate")
elif (
    len(license_plate) == 7
    and license_plate[0] >= "0"
    and license_plate[0] <= "9"
    and license_plate[1] >= "0"
    and license_plate[1] <= "9"
    and license_plate[2] >= "0"
    and license_plate[2] <= "9"
    and license_plate[3] >= "0"
    and license_plate[3] <= "9"
    and license_plate[4] >= "A"
    and license_plate[4] <= "Z"
    and license_plate[5] >= "A"
    and license_plate[5] <= "Z"
    and license_plate[6] >= "A"
    and license_plate[6] <= "Z"
):
    print("The plate is valid older style plate")
else:
    print("The plate is not valid")