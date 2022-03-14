import re
from collections import defaultdict

with open("origami_data.txt", "r") as f:
    # Parse coordinates
    points = []
    for line in f:
        if line == '\n':
            break
        coord = line.strip().split(',')
        x, y = int(coord[0]), int(coord[1])
        points.append((x, y))

    # Parse first instruction
    instruction_str = f.read()
    result = re.search("([xy])=([0-9]+)", instruction_str)

    if result:
        is_fold_x = result.group(1) == 'x'
        fold_line = int(result.group(2))

        # Create hash map <int, list<int>> of coordinates with x or y coordinate keys matching fold axis
        grid_map = defaultdict(set)
        if is_fold_x:
            for x, y in points:
                grid_map[x].add(y)
        else:
            for x, y in points:
                grid_map[y].add(x)

        # Subtract dots that overlap after first fold
        visited = {fold_line}
        dot_count = len(points) - len(grid_map[fold_line])
        for index, coord_set in grid_map.items():
            if index in visited:
                continue
            compare_index = (fold_line - (index - fold_line))
            if compare_index in grid_map:
                overlap_set = coord_set.intersection(grid_map[compare_index])
                dot_count -= len(overlap_set)
                visited.add(compare_index)

        print(dot_count)
