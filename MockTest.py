# Define an empty list to store the fish and weight
fish_data = []

# User can input any number for the entries for fishes
num_of_entries = int(input("Number of entries: "))

# Calculate the weight of the Fish
def calculate_weight(length, girth):
    weight = (girth * girth * length) / 800
    return round(weight, 2)

# Create a validation where it prompts the user to key in a valid numeric number for (length, girth) 
def numeric_value(length_and_girth, length_and_girth_error_message):
    while True:
        try:
            value = float(input(length_and_girth))
            return value
        except ValueError:
            print(length_and_girth_error_message)

# Classify the fish based on the weight
def categorise_weight(fish):
    if fish <= 41:
        return "Small Fish"
    elif 42 <= fish <= 99:
        return "Medium Fish"
    elif 100 <= fish <= 174:
        return "Big Fish"
    else:
        return "Giant Fish"

# Calculate the weight of the Fish
def calculate_weight(length, girth):
    weight = (girth * girth * length) / 800
    return round(weight, 2)

# Prompt the User input the name of the fish, length and girth of the fish.
# If invalid input is entered for length and girth it will ask the user to re-enter again.
for i in range(num_of_entries):
    fish_name = input(f"Enter the name of the Fish {i+1}: ")
    length = numeric_value(f"Enter the length of {fish_name}: ", "Invalid input, please re-enter a numeric value for length.")
    girth = numeric_value(f"Enter the girth of {fish_name}: ", "Invalid input, please re-enter a numeric value for girth.")

    weight = calculate_weight(length, girth)
    classification = categorise_weight(weight)

    fish_data.append({
        "Fish Name": fish_name,
        "Weight(pounds)": weight,
        "Classification": classification
    })
    
    # Display the fish data
    print("\nFish Data:")
    print(f"The name of the Fish is: {fish_name}")
    print(f"The weight of the Fish is: {weight} pounds")
    print(f"The Fish is classified as: {classification}")
    print("")
