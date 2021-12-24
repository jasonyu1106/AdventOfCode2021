horizontal = 0
depth = 0
aim = 0
with open("navigation_data.txt", "r") as f:
    for line in f:
        data = line.split()
        if data[0] == "forward":
            horizontal += int(data[1])
            depth += aim * int(data[1])
        elif data[0] == "down":
            aim += int(data[1])
        elif data[0] == "up":
            aim -= int(data[1])
        else:
            print("Direction unrecognized\n")
    print("Horizontal: ", horizontal, " Depth: ", depth, "Product: ", horizontal*depth, "Aim: ", aim)