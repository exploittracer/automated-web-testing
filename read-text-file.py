# Open the file and read all filenames into a list
with open('file-list.txt', 'r') as file:
    filenames = [line.strip() for line in file if line.strip()]

# Print the list of filenames
for file in filenames:
    print(file)