# Get names
with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()

# Get letter template
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

# Iterate over names and create custom letter
for name in names:
    current_name = name.strip()
    custom_letter = letter.replace("[name]", current_name)

    with open(f"Output/ReadyToSend/letter_for_{current_name}.txt", mode="w") as new_data:
        new_data.write(custom_letter)
