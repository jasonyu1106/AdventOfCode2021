with open("segment_display_data.txt", "r") as f:
    unique_seg_count = 0
    # 2: Digit 1, 4: Digit 4, 3: Digit 7, 7: Digit 8
    unique_num_seg_set = {2, 4, 3, 7}
    for line in f:
        io_data = line.strip().split(" | ")
        inputs, outputs = io_data[0], io_data[1]
        input_data = inputs.split(" ")
        output_data = outputs.split(" ")

        for digit_signal in output_data:
            if len(digit_signal) in unique_num_seg_set:
                unique_seg_count += 1

print(unique_seg_count)
