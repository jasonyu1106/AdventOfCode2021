incCount = 0
windowSize = 3
window = []

with open("sonardata.txt", "r") as f:
    for i in range(windowSize):
        window.append(int(f.readline().strip()))
    for line in f:
        prevSum = sum(window)
        window.pop(0)
        window.append(int(line.strip()))
        newSum = sum(window)
        if newSum > prevSum:
            incCount += 1

print(incCount)
