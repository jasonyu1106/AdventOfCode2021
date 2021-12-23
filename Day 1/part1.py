incCount = 0;
with open("sonardata", "r") as f:
    prevDepth = int(f.readline().strip())
    for line in f:
        newDepth = int(line.strip())
        if newDepth > prevDepth:
            incCount += 1
        prevDepth = newDepth
print(incCount)



