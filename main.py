import re


#### Config ####
inputFilePath = 'input.txt'
outputFilePath = 'output.txt'


class WeighingMachine:
    def __init__(self):
        self.load = 0.0  # 0 grams at begining
        pass

    def addLoad(self, weight):
        self.load += weight

    # This function must be called once in order to fulfill requirement of the test
    def getTotalWeight(self):
        return self.load


#### Main ####
weighingMachine = WeighingMachine()

totalSacks = 0
with open(inputFilePath, 'r') as inputFile:
    for line in inputFile:
        # validate each line format and extract the sack number
        match = re.search(r'Sack-(\d+),\s*(\d+)', line)
        if match == None:
            raise Exception("Invalid format at line: %s" % line)

        # extract sack number and its weight
        sackNumber = int(match[1])
        sackWeight = int(match[2])
        print('Sack (%d) => weight (%d)' % (sackNumber, sackWeight))

        # add n fraction (100/n) of sack to the weighing machine
        weighingMachine.addLoad(sackWeight/sackNumber)
        totalSacks += 1


# If all the sacks would have real weights, then the ideal total weight must be:
# ITW = (100/1) + (100/2) + (100/3) + ... (100/k)
# We will have following total weight:
# TW  = (100/1) + (100/2) + ... + X + ...+(100/k) , where X = (90/N)

# ITW - TW = (100/N) - (90/N) = (10/N)
# N = 100 / (ITW - TW) / 10
# Output: N is the sack number

# REAL TOTAL WEIGHT
totalWeight = weighingMachine.getTotalWeight()
print('The total weight is %f' % totalWeight)

# IDEAL TOTAL WEIGHT
idealTotalWeight = sum([100/i for i in range(1, totalSacks+1)])
print('Ideal total weight: ', idealTotalWeight)

# Compute N
N = round(100.0 / (idealTotalWeight - totalWeight) / 10.0)
print('N: ', N)


# compute the output
with open(outputFilePath, 'w') as outputFile:
    print('Sack-%d, 90' % N, file=outputFile)
    for idx in range(1, totalSacks+1):
        if(idx == N):
            continue
        print('Sack-%d, 100' % idx, file=outputFile)
