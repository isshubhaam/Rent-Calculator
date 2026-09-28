## Inputs we need from the user 
# Total Rent
# Total food ordered for snacking
# Electricity bill
# Charge per unit 
# Persons lIving in room / flat

## Output
# Total amount you've to pay is 

rent = int(input("Enter your hostel /flat rent:- "))
food = int(input("Enter the amount of food orderrd:- "))
electricity_bill = int(input("Enter the electricity bill:- "))
charge_per_unit = int(input("Enter the charge per unit:- "))
persons = int(input("Enter the number of persons living in room/flat:-"))

total_bill = electricity_bill * charge_per_unit

output = (food + rent + total_bill)

print(f"Total amount you've to pay is {output/persons}")
