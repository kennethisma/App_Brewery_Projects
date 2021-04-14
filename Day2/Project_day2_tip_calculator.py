print("\tWelcome to the tip calculator")

bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15"))

split_bill = int(input("How many people to split the bill? "))

tip_percentage = tip / 100

total_tip = bill * tip_percentage

total_bill = bill + total_tip

bill_splited = total_bill / split_bill

bill_rounded = round(bill_splited, 2)

print("{:.2f}".format(bill_rounded))
