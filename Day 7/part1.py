import math
import statistics

with open("crab_locations", "r") as f:
    data = f.readline().split(",")

data = [int(val) for val in data]
min_position = min(data)
max_position = max(data)

ideal_pos = -1
min_fuel = math.inf
for pos in range(min_position, max_position+1):
    fuel = 0
    for val in data:
        fuel += abs(pos - val)
    if fuel < min_fuel:
        ideal_pos = pos
        min_fuel = fuel

print("Brute Force -> Position:", ideal_pos, "\tMinimum Fuel:", int(min_fuel))
print("Median -> Position:", int(statistics.median(data)))
