import random
class WeightedMap(object):
    def __init__(self):
        self.totalWeight = 0
        self.entries = {}

    def add(self, entry, weight):
        oldWeight = self.entries.get(entry, 0)
        self.entries[entry] = weight
        self.totalWeight += weight - oldWeight

    def get(self, entry):
        return self.entries.get(entry, 0)

    def randomGet(self):
        rand = random.random()
        print("Random number " + str(rand))
        lastNearestRand = 1.1
        lastNearestEntry = None
        probs = {}
        for eachKey in self.entries.keys():
            eachProb = self.entries[eachKey] / self.totalWeight
            probs[eachProb] = eachKey

        sortedProbs = sorted(probs.keys())
        accProbs = {}
        accProbs[sortedProbs[0]] = probs[sortedProbs[0]]
        runningAccRand = sortedProbs[0]
        for i in range(1, len(sortedProbs)):
            accProbs[sortedProbs[i]+runningAccRand] = probs[sortedProbs[i]]
            runningAccRand += sortedProbs[i]

        for eachAccProb in accProbs.keys():
            if eachAccProb > rand:
                if abs(eachAccProb-rand) < abs(lastNearestRand-rand):
                    lastNearestRand = eachAccProb
                    lastNearestEntry = accProbs[eachAccProb]

        return lastNearestEntry

test = WeightedMap()
test.add("Goog", 20)
test.add("Amzn", 10)
test.add("Msft", 30)
test.add("Appl", 15)
test.add("Att", 25)

print(test.randomGet())