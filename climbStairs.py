def climbStairs(stairSteps):
    if stairSteps <= 0:
        return 0
    if stairSteps == 1:
        return 1
    if stairSteps == 2:
        return 2
    if stairSteps == 3:
        return 1+2+1

    return climbStairs(stairSteps-1)+climbStairs(stairSteps-2)+climbStairs(stairSteps-3)

print(climbStairs(4))
print(climbStairs(6))
print(climbStairs(12))
