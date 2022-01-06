def increment_energy(energy_map, j, i):
    if energy_map[j][i] == -1:
        return 0

    flash = 0
    energy_map[j][i] += 1
    if energy_map[j][i] > 9:
        # Set value to -1 to identify flash during step
        energy_map[j][i] = -1
        flash = increment_adjacent(energy_map, j, i) + 1

    return flash


def increment_adjacent(energy_map, j, i):
    count = 0
    if j > 0:
        count += increment_energy(energy_map, j - 1, i)
    if j < len(energy_map) - 1:
        count += increment_energy(energy_map, j + 1, i)
    if i > 0:
        count += increment_energy(energy_map, j, i - 1)
    if i < len(energy_map[j]) - 1:
        count += increment_energy(energy_map, j, i + 1)
    if j > 0 and i > 0:
        count += increment_energy(energy_map, j - 1, i - 1)
    if j > 0 and i < len(energy_map[j]) - 1:
        count += increment_energy(energy_map, j - 1, i + 1)
    if j < len(energy_map) - 1 and i > 0:
        count += increment_energy(energy_map, j + 1, i - 1)
    if j < len(energy_map) - 1 and i < len(energy_map[j]) - 1:
        count += increment_energy(energy_map, j + 1, i + 1)

    return count


def reset_grid(energy_map):
    # Replace all -1 values with 0, to prepare next step
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == -1:
                grid[j][i] = 0


with open("energy_level_data.txt", "r") as f:
    grid = []
    for line in f:
        grid.append([int(num) for num in list(line.strip())])

STEPS = 100

flash_count = 0

for _ in range(STEPS):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            flash_count += increment_energy(grid, j, i)

    reset_grid(grid)

print(grid)
print(flash_count)
