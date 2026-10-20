filename = "missing_file.csv"

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")
    print("Please check the filename and try again.")