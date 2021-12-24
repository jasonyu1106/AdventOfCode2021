import math

with open("crab_locations.txt", "r") as f:
    data = f.readline().split(",")

data = [int(val) for val in data]
min_position = min(data)
max_position = max(data)

ideal_pos = -1
min_fuel = math.inf
for pos in range(min_position, max_position+1):
    fuel = 0
    for val in data:
        dist = abs(pos - val)
        fuel += (dist*(dist + 1))/2
    if fuel < min_fuel:
        ideal_pos = pos
        min_fuel = fuel

print("Position:", ideal_pos, "\tMinimum Fuel:", int(min_fuel))