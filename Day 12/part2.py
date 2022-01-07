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


def count_paths(cave: Cave, visited: [], path: [], has_visit_small_cave: bool):
    if cave.name == "start" or cave.name in visited and has_visit_small_cave:
        # Terminate path if traversed to start cave OR a visited small cave after already visiting a small cave twice
        return 0
    path = path + [cave.name]
    if cave.name == "end":
        # End cave reached, return and increment counter by 1
        print(path)
        return 1

    flag = has_visit_small_cave
    if not cave.isLargeCave:
        if cave.name in visited:
            # Small cave visited twice in this path, no more repeated small caves until end
            flag = True
        visited = visited + [cave.name]

    counter = 0
    for adjacent in cave.adjacent:
        counter += count_paths(adjacent, visited, path, flag)

    return counter


graph = CaveGraph()
with open("branch_data.txt", "r") as f:
    for line in f:
        caves = line.strip().split("-")
        graph.add_edge(caves[0], caves[1])

startCave = graph.caves["start"]
paths = 0
for cave in startCave.adjacent:
    paths += count_paths(cave, ["start"], ["start"], False)

print(paths)
