def calculate_oxygen(filtered_input, bit_index):
    if bit_index == 12 or len(filtered_input) == 1:
        return filtered_input

    count = 0
    for bit_string in filtered_input:
        count = count+1 if bit_string[bit_index] == '1' else count-1

    # filter by most common bit
    if count >= 0:
        # filter by bit 1
        new_list = list(filter(lambda bits: bits[bit_index] == '1', filtered_input))
    else:
        # filter by bit 0
        new_list = list(filter(lambda bits: bits[bit_index] == '0', filtered_input))
    return calculate_oxygen(new_list, bit_index + 1)


def calculate_co2(filtered_input, bit_index):
    if bit_index == 12 or len(filtered_input) == 1:
        return filtered_input

    count = 0
    for bit_string in filtered_input:
        count = count+1 if bit_string[bit_index] == '1' else count-1

    # filter by least common bit
    if count >= 0:
        # filter by bit 0
        new_list = list(filter(lambda bits: bits[bit_index] == '0', filtered_input))
    else:
        # filter by bit 1
        new_list = list(filter(lambda bits: bits[bit_index] == '1', filtered_input))
    return calculate_co2(new_list, bit_index + 1)


data = []
with open("diagnostic_binary", "r") as f:
    for line in f:
        data.append(line.strip())

oxygenRating = int(calculate_oxygen(data, 0)[0], 2)
co2ScrubberRating = int(calculate_co2(data, 0)[0], 2)

print("Life Support Rating: ", oxygenRating * co2ScrubberRating)
