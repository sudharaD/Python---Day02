while True:

    try:

        print("Welcome to the tip calculator")

        total_bill = float(input("What was the total bill? $"))
        tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
        people_count = int(input("How many people to split the bill? "))

        tip_amount = total_bill * (tip_percentage / 100)
        new_total_bill = total_bill + tip_amount

        # Can format in both ways
        amount_for_an_individual = "{:.2f}".format(new_total_bill / people_count)
        # amount_for_an_individual = format(new_total_bill / people_count, '.2f')

        message = f"Each person should pay: ${amount_for_an_individual}"

        print(message)

        break

    except:

        print("Please enter appropriate values as inputs")