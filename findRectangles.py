'''
Given a set of tuplets((x1,y1), (x2,y2)) representing the top left and
bottom right corners of a set of rectangles that overlap.  Find the
set of tuplets that represent the set of rectangles, which
cover the areas covered by these overlapping rectangles. i.e.
from the input set, eliminate any rectangles that are completely
covered by other rectangles.
'''
import sys

def buildHorizontalEdges(corner):
    topLeft = corner[0]
    bottomRight = corner[1]
    return [(topLeft[1], (topLeft[0], bottomRight[0])), (bottomRight[1], (topLeft[0], bottomRight[0]))]

def buildVerticalEdges(corner):
    topLeft = corner[0]
    bottomRight = corner[1]
    return [(topLeft[0], (bottomRight[1], topLeft[1])), (bottomRight[0], (bottomRight[1], topLeft[1]))]

def buildEdges(corners):
    tops = []
    bottoms = []
    lefts = []
    rights = []

    for i in range(len(corners)):
        # corner in form of ((x1,y1),(x2,y2)) where the first entry
        # of the tuple is the top left and the second is the bottom right
        horizontals = buildHorizontalEdges(corners[i])
        verticals = buildVerticalEdges(corners[i])
        tops.append(horizontals[0])
        bottoms.append(horizontals[1])
        lefts.append(verticals[0])
        rights.append(verticals[1])

    return [tops, rights, bottoms, lefts]

def scanAndPickEdges(edges, orientation):
    # edges are arranged in proper order
    requiredEdges = []
    maxFrom = sys.maxsize
    minTo = 1-sys.maxsize
    for edge in edges:
        if edge[1][0] < maxFrom or edge[1][1] > minTo:
            requiredEdges.append(edge)
        if edge[1][0] < maxFrom:
            maxFrom = edge[1][0]
        if edge[1][1] > minTo:
            minTo = edge[1][1]

    requiredCorners = []
    for edge in requiredEdges:
        if orientation == "top":
            requiredCorners.append((edge[1][0], edge[0]))
        elif orientation == "bottom":
            requiredCorners.append((edge[1][1], edge[0]))
        elif orientation == "left":
            requiredCorners.append((edge[0], edge[1][1]))
        else:
            requiredCorners.append((edge[0], edge[1][0]))
    return requiredCorners

def findMinRectangles(rectangles):
    corners = []
    for rectangle in rectangles:
        corners.append(rectangle[0])
        corners.append(rectangle[1])

    edges = buildEdges(corners)
    requiredCorners = set()
    requiredCorners.union(scanAndPickEdges(edges[0], "top"))
    requiredCorners.union(scanAndPickEdges(edges[1], "right"))
    requiredCorners.union(scanAndPickEdges(edges[2], "bottom"))
    requiredCorners.union(scanAndPickEdges(edges[3], "left"))

    requiredRectangles = []
    # from the requiredCorners, retrieve the original rectangles
    for corner in requiredCorners:
        for rectangle in rectangles:
            if rectangle[0] == corner or rectangle[1] == corner:
                requiredRectangles.append(rectangle)

    return requiredRectangles





