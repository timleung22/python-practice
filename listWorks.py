class Elem:
    def __init__(self, value=None, nextElem=None):
        self.value = value
        self.nextElem = nextElem

    def reverse(self, prevElem):
        next = self.nextElem
        self.nextElem = prevElem

        if next != None:
            return next.reverse(self)
        else:
            return self

    def mergeRecur(self, another):
        if another is None:
            return self

        if self.value <= another.value:
            self.nextElem = another.mergeRecur(self.nextElem)
            return self
        else:
            another.nextElem = self.mergeRecur(another.nextElem)
            return another

    def removeDups(self):
        if self.nextElem is None:
            return self

        self.nextElem = self.nextElem.removeDups()
        prev = None
        curr = self
        while curr is not None:
            if curr.value == self.value:
                prev.nextElem = curr.nextElem
            prev = curr
            curr = curr.nextElem

        return self

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def setHead(self, head):
        self.head = head

    def add(self, val):
        newElem = Elem(val)
        if self.head == None:
            self.head = newElem
            self.tail = newElem
        self.tail.nextElem = newElem
        self.tail = newElem
        self.length += 1

    def print(self):
        cursor = self.head
        while cursor != None:
            print(cursor.value)
            cursor = cursor.nextElem

    def reverse(self):
        prevNode = None
        nextNode = None
        currentNode = self.head
        while currentNode != None:
            nextNode = currentNode.nextElem
            currentNode.nextElem = prevNode
            prevNode = currentNode
            currentNode = nextNode

        self.head = prevNode

    def removeDuplicates(self):
        self.head = self.head.removeDup()

    def reverseRecursive(self, curr, next):
        if next.nextElem == None:
            return next
        newHead = self.reverseRecursive(next, next.nextElem)
        newHead.next = next

    def splitAlternate(self):
        if self.head.nextElem is None:
            return (self, None)

        firstSplitted = MyList()
        secondSplitted = MyList()

        curr = self.head
        next = curr.nextElem
        firstSplitted.setHead(curr)
        secondSplitted.setHead(next)
        while next is not None:
            curr.nextElem = next.nextElem
            curr = next
            next = curr.nextElem

        return (firstSplitted, secondSplitted)

    def rearrange(self):
        slow = self.head
        fast = self.head

        while fast != self.tail:
            slow = slow.nextElem
            fast = fast.nextElem
            if fast != None:
                fast = fast.nextElem
        # now slow is at mid, fast at end
        frontCursor = self.head
        while frontCursor != slow:
            endCursor = slow
            endCursorPrev = endCursor
            while endCursor.nextElem != None:
                endCursorPrev = endCursor
                endCursor = endCursor.nextElem
            temp = frontCursor.nextElem
            frontCursor.nextElem = endCursor
            endCursor.nextElem = temp
            endCursorPrev.nextElem = None
            frontCursor = temp
        self.tail = slow

    def mergeRecur(self, another):
        merged = self.head.mergeRecur(another.head)
        self.head = merged

    def merge(self, another):
        # list 1 is 1,3,5,7
        # list 2 is 2,4,6,8

        c1 = self.head
        c2 = another.head
        prev1 = None
        while c1 != None and c2 != None:
            if c1.value < c2.value:
                prev1 = c1
                c1 = c1.nextElem
            else:
                prev1.nextElem = c2
                temp = c2.nextElem
                c2.nextElem = c1
                c1 = c2
                c2 = temp

        if c2 != None:
            prev1.nextElem = c2
        self.length += another.length


    def swapForK(self, k):
        self.head = self.swapRecursively(self.head, k)

    def swapRecursively(self, begin, k):
        if begin == None:
            return begin

        if k == 0:
            return begin

        begin.nextElem = self.swapRecursively(begin.nextElement, k-1)
        return begin

    def swapIteratively(self, begin, k):
        i = 0
        curr = begin
        prev = None
        while i < k and curr is not None:
            next = curr.nextElem
            curr.nextElem = prev
            prev = curr
            curr = next
            i += 1

        return prev

    def reverseR(self):
        self.head = self.head.reverse(None)

myList = MyList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.reverseR()
myList.print()

print("Merging 2 sorted lists")
myList = MyList()
myList.add(1)
myList.add(4)
myList.add(7)
myList.add(11)
secondList = MyList()
secondList.add(2)
secondList.add(3)
secondList.add(9)
secondList.add(17)

myList.mergeRecur(secondList)
myList.print()


print("Swapping every 4 nodes")
myList = MyList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.add(6)
myList.add(7)
myList.add(8)
myList.add(9)
myList.add(10)

#myList.swapForK(4)
splitted = myList.splitAlternate()
splitted[0].print()
splitted[1].print()