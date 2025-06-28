def total_calc():
    bill_amount = float(input("Enter the bill amount: "))
    tip_perc = float(input("Enter the tip percentage: "))
    tip_amout = bill_amount * (tip_perc / 100)
    total_amount = bill_amount + tip_amout
    print("Bill amount:", bill_amount)
    print("Tip(", tip_perc, "%):", tip_amout)
    print("Total amount to pay:", total_amount)
total_calc()