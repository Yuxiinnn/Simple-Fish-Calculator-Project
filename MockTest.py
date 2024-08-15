# Get User Input
Fish_Name1 = input("Enter the name of Fish: ")
Length1 = float(input(f"Enter the length of the {Fish_Name1}: "))
Girth1 = float(input(f"Enter the girth of the {Fish_Name1}: "))

Fish_Name2 = input("Enter the name of the Fish: ")
Length2 = float(input(f"Enter the length of the {Fish_Name2}: "))
Girth2 = float(input(f"Enter the girth of the {Fish_Name2}: "))

# Calculate the weight of the Fish
def calculate_weight(Length1, Girth1):
    Weight1 = (Girth1 * Girth1 * Length1) / 800
    return round(Weight1, 2)

def calculate_weight(Length2, Girth2):
    Weight2 = (Girth2 * Girth2 * Length2) / 800
    return round(Weight2, 2)

# Calculate the weight using the Function
Weight1 = calculate_weight(Length1, Girth1)
Weight2 = calculate_weight(Length2, Girth2)

# Classify the fish based on the weight
if Weight1 <= 41:
    classification1 = ("Small Fish")
elif Weight1 <= 99:
    classification1 = ("Medium Fish")
elif Weight1 <= 174:
    classification1 = ("Big Fish")
else:
    classification1 = ("Giant Fish")

if Weight2 <= 41:
    classification2 = ("Small Fish")
elif Weight2 <= 99:
    classification2 = ("Medium Fish")
elif Weight2 <= 174:
    classification2 = ("Big Fish")
else:
    classification2 = ("Giant Fish")

print(f"The weight of the fish for {Fish_Name1} is: {Weight1} pounds")
print(f"The fish is classified as: {classification1}")

print(f"The weight of the fish for {Fish_Name2} is {Weight2} pounds")
print(f"The fish is classified as: {classification2}")