with open("vent_data.txt", "r") as f:
    vent_data = []
    for line in f:
        data = line.strip().split(" -> ")
        coord_list = [pair.split(",") for pair in data]
        coordinates = [int(val) for coord_str in coord_list for val in coord_str]
        vent_data.append(coordinates)

dict = {}
for vent_values in vent_data:
    x1, y1, x2, y2 = [value for value in vent_values]
    if x1 == x2:
        # Vertical Vent
        if y1 > y2:
            # swap for range()
            y1, y2 = y2, y1

        for i in range(y1, y2+1):
            if not (x1, i) in dict:
                dict[(x1, i)] = 1
            else:
                dict[(x1, i)] += 1
    elif y1 == y2:
        # Horizontal Vent
        if x1 > x2:
            # swap for range()
            x1, x2 = x2, x1

        for i in range(x1, x2 + 1):
            if not (i, y1) in dict:
                dict[(i, y1)] = 1
            else:
                dict[(i, y1)] += 1
    else:
        # Diagonal Vent
        # Assign left-most point to point 1
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        j = y1
        if y1 < y2:
            # Diagonal Up & Right
            for i in range(x1, x2+1):
                if not (i, j) in dict:
                    dict[(i, j)] = 1
                else:
                    dict[(i, j)] += 1
                j += 1
        else:
            # Diagonal Down & Right
            for i in range(x1, x2 + 1):
                if not (i, j) in dict:
                    dict[(i, j)] = 1
                else:
                    dict[(i, j)] += 1
                j -= 1

counter = 0
for value in dict.values():
    if value > 1:
        counter += 1

print(counter)
