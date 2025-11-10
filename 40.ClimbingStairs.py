''' wap to implement the climbing stairs problem '''
''' given a fixed number of steps of staircase, you need to find the number of ways to reach the top.
    you can climb either 1 or 2 steps at a time '''

def climbStairs(steps, memo={}):
    if steps == 0:                              # means you're at top of the staircase. 
        return 1                                # achieved the result in exactly 1 way
    elif steps < 0:                             # invalid stair count. condition to handle the scenario
        return 0
    elif steps in memo:                         # step count exists in memory
        return memo[steps]                      # return the count of ways to climb, from memory

    memo[steps] = climbStairs(steps-1, memo) + climbStairs(steps-2, memo)       # update the count of new ways to climb, in memory
    return memo[steps]                          # return the max valid ways to reach the top
    
print(climbStairs(5))