# Movie Ticket Price
# variables to store the user age and membership
age = int(input("What is your age?"))
membership = (input("Do you have a membership? Enter Y or N: ")).upper()
# else-if statments to print certain things
if age < 18:
    print("Youth ticket is $10")

if age >= 18:
    if age>=65:
        print("Senior discount price is $8.")
    else:
        if membership == "Y":
            print("Discounted adult ticket price is $12")
        else:
            print("Regular adult ticket is $15")

#Energy Usage Billing
total_energy_usage = int(input("What is your total energy usage in kWh? Enter a value:"))
low_income = (input("Are you registered as a low-income household? Enter Y or N: ")).upper()

if total_energy_usage<200:
    if low_income == "Y":
        print("Discounted rate of $0.08/kWh applies.")
    else:
        print("Standard rate of $0.10/kWh applies.")

elif total_energy_usage>=200:
    if total_energy_usage<=500:
        print("Medium usage rate of $0.12/kWh applies.")
else:
    if low_income == "Y":
        print("Discounted high usage rate of $0.15/kWh applies.")
    else:
        print("High usage rate of $0.20/kWh applies.")
