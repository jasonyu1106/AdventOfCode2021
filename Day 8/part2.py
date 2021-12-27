# Return dictionary mapping input set to output digit
def decode_input(input_data : []):
    input_dict = {}
    output_dict = {}

    # Known mapping of number of segments to output digit
    unique_num_seg_dict = {2: 1,
                           4: 4,
                           3: 7,
                           7: 8}

    # Convert input data to list of sets
    input_data_sets = [frozenset(signal_str) for signal_str in input_data]

    # Identify signals representing the digits with unique number of segments
    unique_signals = []
    for digit_signal in input_data_sets:
        num_seg = len(digit_signal)
        if num_seg in unique_num_seg_dict:
            input_dict[digit_signal] = unique_num_seg_dict[num_seg]
            output_dict[unique_num_seg_dict[num_seg]] = digit_signal
            unique_signals.append(digit_signal)

    # Remove known digital signals (1, 4, 7, 8) sets
    unknown_signals = [signal for signal in input_data_sets if signal not in unique_signals]

    # Perform deduction on remaining signals (0, 2, 3, 5, 6, 9)

    # Identify digit 6
    for digit_signal in unknown_signals:
        if len(digit_signal) == 6:
            # Difference between 8 and 1 signals
            diff = output_dict[8] - output_dict[1]
            if diff.issubset(digit_signal):
                # Signal for digit 6
                input_dict[digit_signal] = 6
                output_dict[6] = digit_signal
                unknown_signals.remove(digit_signal)
                break

    # Identify digit 9
    for digit_signal in unknown_signals:
        if len(digit_signal) == 6 and output_dict[4].issubset(digit_signal):
            # Signal for digit 9
            input_dict[digit_signal] = 9
            output_dict[9] = digit_signal
            unknown_signals.remove(digit_signal)
            break

    # Identify digit 0
    for digit_signal in unknown_signals:
        if len(digit_signal) == 6:
            # Signal for digit 0
            input_dict[digit_signal] = 0
            output_dict[0] = digit_signal
            unknown_signals.remove(digit_signal)
            break

    # Identify digit 3
    for digit_signal in unknown_signals:
        if output_dict[1].issubset(digit_signal):
            # Signal for digit 3
            input_dict[digit_signal] = 3
            output_dict[3] = digit_signal
            unknown_signals.remove(digit_signal)
            break

    # Identify digit 5
    for digit_signal in unknown_signals:
        if len(output_dict[6] - digit_signal) == 1:
            # Signal for digit 5
            input_dict[digit_signal] = 5
            output_dict[5] = digit_signal
            unknown_signals.remove(digit_signal)
            break

    # Identify digit 2
    for digit_signal in unknown_signals:
        if len(output_dict[6] - digit_signal) == 2:
            # Signal for digit 5
            input_dict[digit_signal] = 2
            output_dict[2] = digit_signal
            unknown_signals.remove(digit_signal)
            break

    # All signals identified
    assert not unknown_signals

    return input_dict


output_sum = 0
with open("segment_display_data.txt", "r") as f:
    for line in f:
        io_data = line.strip().split(" | ")
        inputs, outputs = io_data[0], io_data[1]
        input_data = inputs.split(" ")
        output_data = outputs.split(" ")

        signal_dict = decode_input(input_data)
        output_digits = []
        for digit_signal_str in output_data:
            digit_signal = frozenset(digit_signal_str)
            output_digits.append(signal_dict[digit_signal])

        output_sum += int("".join([str(digit) for digit in output_digits]))

print(output_sum)



