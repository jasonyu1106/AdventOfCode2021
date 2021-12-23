binarySize = 12
binaryCounter = [0] * binarySize

with open("diagnostic_binary", "r") as f:
    for line in f:
        for index, bit in enumerate(line.strip()):
            if bit == "0":
                binaryCounter[index] -= 1
            elif bit == "1":
                binaryCounter[index] += 1
            else:
                print("Invalid bit")

gammaRateList = []
for counter in binaryCounter:
    if counter > 0:
        gammaRateList.append("1")
    elif counter < 0:
        gammaRateList.append("0")
    else:
        print("Equal number of 0,1 bits")

gammaRateString = "".join(gammaRateList)
gammaRate = int(gammaRateString, 2)
mask = int("".join(["1"] * binarySize), 2)
epsilonRate = gammaRate ^ mask

print("Gamma: ", gammaRate, "Epsilon: ", epsilonRate, "Power Consumption: ", gammaRate*epsilonRate)

