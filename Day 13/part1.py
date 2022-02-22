# with open("origami_data.txt", "r") as f:
#     # Parse coordinates
#     coord_list = []
#     max_x, max_y = 0, 0
#     for line in f:
#         if line == '\n':
#             break
#         coord = line.strip().split(',')
#         x, y = int(coord[0]), int(coord[1])
#         max_x = max(max_x, x)
#         max_y = max(max_y, y)
#         coord_list.append((x, y))
#
#     grid = [[0 for _ in range(max_x)] for _ in range(max_y)]
#     # Parse instructions
#     for line in f:
#         print(line)
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
        grid_map = defaultdict(list)
        for x, y in points:
            if is_fold_x:
                grid_map[x].append(y)
            else:
                grid_map[y].append(x)

