with open("ascii_data.txt", "r") as file:
    ascii_art = file.read()

for line in ascii_art.splitlines():
    print(line)