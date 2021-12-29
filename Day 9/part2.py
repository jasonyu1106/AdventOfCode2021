def is_lowest_point(matrix: [], x, y):
    if matrix[y][x] == 9:
        return False

    depth = matrix[y][x]

    if y > 0 and depth > matrix[y - 1][x]:
        return False
    if y < len(matrix) - 1 and depth > matrix[y + 1][x]:
        return False
    if x > 0 and depth > matrix[y][x - 1]:
        return False
    if x < len(matrix[y]) - 1 and depth > matrix[y][x + 1]:
        return False

    return True


def calculate_basin_size(matrix, x, y):
    if matrix[y][x] == 9:
        return 0

    # Mark as visited with digit 9
    matrix[y][x] = 9

    size = 1
    if y > 0:
        size += calculate_basin_size(matrix, x, y - 1)
    if y < len(matrix) - 1:
        size += calculate_basin_size(matrix, x, y + 1)
    if x > 0:
        size += calculate_basin_size(matrix, x - 1, y)
    if x < len(matrix[y]) - 1:
        size += calculate_basin_size(matrix, x + 1, y)

    return size


matrix = []
with open("elevation_data.txt", "r") as f:
    for line in f:
        matrix.append([int(digit) for digit in list(line.strip())])

basin_sizes = []
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if is_lowest_point(matrix, x, y):
            basin_sizes.append(calculate_basin_size(matrix, x, y))

print(basin_sizes)
print(matrix)

# Product of three largest depths
product = 1
for _ in range(3):
    largest = max(basin_sizes)
    product *= largest
    basin_sizes.remove(largest)

print(product)
