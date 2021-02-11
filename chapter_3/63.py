# Average
num = int(
    input(
        "Enter the numbers and calculate the sum, insert a 0 to end the insert values: "
    )
)
if num != 0:
    n_message = 1
    sum_num = 0
    while num != 0:
        sum_num += num
        average = sum_num / n_message
        num = int(input())
        n_message = n_message + 1
    print("The average is %.2f" % average)
else:
    print("you have entered a 0, re-run the program again...")