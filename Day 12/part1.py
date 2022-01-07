class Cave:
    def __init__(self, name: str):
        self.name = name
        self.isLargeCave = name.isupper()
        self.adjacent = []

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)


class CaveGraph:
    def __init__(self):
        self.caves = {}

    def add_edge(self, name1: str, name2: str):
        if name1 not in self.caves:
            self.caves[name1] = Cave(name1)
        if name2 not in self.caves:
            self.caves[name2] = Cave(name2)
        self.caves[name1].add_neighbor(self.caves[name2])
        self.caves[name2].add_neighbor(self.caves[name1])


def count_paths(cave: Cave, visited: [], path: []):
    if cave.name in visited:
        # Terminate path if traversed to a visited cave (start or repeated small cave)
        return 0
    # Create and update a copy of path for recursive call
    path = path + [cave.name]
    if cave.name == "end":
        # End cave reached, return and increment counter by 1
        print(path)
        return 1
    if not cave.isLargeCave:
        # Create and update a copy of visited caves for recursive call
        visited = visited + [cave.name]

    counter = 0
    for adjacent in cave.adjacent:
        counter += count_paths(adjacent, visited, path)

    return counter


graph = CaveGraph()
with open("branch_data.txt", "r") as f:
    for line in f:
        caves = line.strip().split("-")
        graph.add_edge(caves[0], caves[1])

startCave = graph.caves["start"]
paths = 0
for cave in startCave.adjacent:
    paths += count_paths(cave, ["start"], ["start"])

print(paths)
