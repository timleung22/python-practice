import heapq

def tryHeap():
    queue = []
    heapq.heappush(queue, (11,'John'))
    heapq.heappush(queue, (4,'Tim'))
    heapq.heappush(queue, (25, 'Peter'))
    heapq.heappush(queue, (6, 'Chris'))

    while len(queue) > 0:
        print (heapq.heappop(queue))


def addDictionaryToHeap(source, dictionary, weight, queue):

    oneMatch = set()
    for eachWord in dictionary:
        # find words that are 1 characters different from source
        for i in range(1, len(source)):
            match = source[0:i]+source[i+1:]
            if match in eachWord:
                oneMatch.add(eachWord)

    for eachMatch in oneMatch:
        dictionary.remove(eachMatch)
    for eachMatch in oneMatch:
        heapq.heappush(queue,(weight, eachMatch))
        addDictionaryToHeap(eachMatch, dictionary, weight+1, queue)

