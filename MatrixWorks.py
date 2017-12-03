class GridOfLights(object):

    def __init__(self):
        pass

    def lightsInGrid(self, gridSize, lights, coords):
        grid = [[0 for x in range(gridSize)] for y in range(gridSize)]

        for light in lights:
            self.installLight(grid, light)

        answers = []
        for coord in coords:
            answers.append(grid[coord[0]][coord[1]] == 1)
        return answers

    def installLight(self, grid, light):
        x = light[0]
        y = light[1]
        grid[x][y] = 1

        self.illuminate(grid, x, y, 1, 0)
        self.illuminate(grid, x, y, 1, 1)
        self.illuminate(grid, x, y, 0, 1)
        self.illuminate(grid, x, y, -1, 1)
        self.illuminate(grid, x, y, -1, 0)
        self.illuminate(grid, x, y, -1, -1)
        self.illuminate(grid, x, y, 0, -1)
        self.illuminate(grid, x, y, 1, -1)

    def illuminate(self, grid, x, y, xOffset, yOffset):
        if x+xOffset < 0 or x+xOffset == len(grid[0]) or y+yOffset < 0 or y+yOffset == len(grid[0]):
            return

        grid[x+xOffset][y+yOffset] = 1
        self.illuminate(grid, x+xOffset, y+yOffset, xOffset, yOffset)


g = GridOfLights()
print(g.lightsInGrid(5, [(0,0),(0,4),(4,0),(4,4)], [(1,1),(1,2),(2,2),(2,3)]))
