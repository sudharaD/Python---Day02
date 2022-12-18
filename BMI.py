
while True:

    try:

        height = float(input("Enter your height in m: "))
        weight = float(input("Enter your weight in kg: "))

        bmi = int(weight / height ** 2)

        bmi = str(bmi)

        print("Your BMI is: " + bmi)

        break

    except:

        print("Please enter values in Integers")

