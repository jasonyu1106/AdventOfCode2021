def evaluate_depth_row(buffer: [], size):
    risk = 0
    for i in range(size):
        depth = buffer[1][i]
        if depth == 9:
            continue

        if i == 0:
            if depth < buffer[0][i] and depth < buffer[1][i + 1] and depth < buffer[2][i]:
                risk += depth + 1
        elif i == size - 1:
            if depth < buffer[0][i] and depth < buffer[1][i - 1] and depth < buffer[2][i]:
                risk += depth + 1
        elif depth < buffer[1][i - 1] and depth < buffer[0][i] and depth < buffer[1][i + 1] \
                and depth < buffer[2][i]:
            risk += depth + 1
    return risk


with open("elevation_data.txt", "r") as f:
    buffer = []
    risk_level = 0
    for line in f:
        depths = [int(digit) for digit in line.strip()]
        if not buffer:
            buffer.append([10 for _ in range(len(depths))])
            buffer.append(depths)
            buffer.append([int(digit) for digit in f.readline().strip()])
        else:
            buffer.append(depths)
            buffer.pop(0)

        risk_level += evaluate_depth_row(buffer, len(depths))

    # Last row
    buffer.pop(0)
    buffer.append([10 for _ in range(len(depths))])
    risk_level += evaluate_depth_row(buffer, len(depths))

print(risk_level)
