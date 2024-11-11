# # Open and read file
# file = open("my_file.txt")
# contents = file.read()  # Reads contents from file
# print(contents)
# file.close()  # Close file to free up computer resources

# To avoid using close() method (no need to remember!), use with keyword
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to file. Must have mode set to write!
# w -> Write and replace entire file
# a -> append to file (like appending to lists!)
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text 2.")

# If file does not exist, system will create it. Only works in write mode
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
