# Cell Phone Bill
phone_plan = 15
minutes_limit = 50
messages_limit = 50
supp_911 = 0.44
percent_sales_tax = 0.05
minutes = int(input("Enter the number of minutes: "))
messages = int(input("Enter the number of messages: "))
add_minutes = minutes - minutes_limit
add_messages = messages - messages_limit
if add_minutes > 0:
    cost_add_minutes = add_minutes * 0.25
else:
    cost_add_minutes = 0
if add_messages > 0:
    cost_add_messages = add_messages * 0.15
else:
    cost_add_messages = 0
tax_month_bill = (
    15 + cost_add_messages + cost_add_minutes + supp_911
) * percent_sales_tax
tot_month_bill = tax_month_bill + 15 + cost_add_messages + cost_add_minutes + supp_911
print(
    "%.2f is the base charge, %.2f is additional minutes charge, %.2f is additional messages charge, %.2f is 911 fee, %.2f is month's tax and %.2f is total month bill"
    % (
        phone_plan,
        cost_add_minutes,
        cost_add_messages,
        supp_911,
        tax_month_bill,
        tot_month_bill,
    )
)
