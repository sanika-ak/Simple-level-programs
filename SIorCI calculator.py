# Menu
print("Interest Calculator")
print("1. Simple Interest")
print("2. Compound Interest")

# User choice
choice = int(input("Choose an option (1 or 2): "))

# Use Input
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (in %): "))
t = float(input("Enter the time period (in years): "))

#If..Elif..Else loop running according to the choosen option
if choice == 1:
    # SI
    si = (p * r * t) / 100 # SI formula
    print("Simple Interest: ",si)

elif choice == 2:
    # CI
    cf = int(input("Enter the number of times interest is compounded per year: "))
    ci = p * (1 + (r / (100 * cf)))**(cf * t) - p # CI formula
    print(f"Compound Interest:",ci)

else: #if the option selcted is wrong
    print("Invalid choice! Please select 1 or 2.")
