
# The traveler is at the upper left corner.
# Target is to reach the lower right corner.
# Possible moves are right and below

# Find total number of ways this can be achieved


# Brut force approach
# Time complexity -> O(2^(n+m))
# Space compexity -> O(n+m)

def gridTraveler_brut(n,m):

    if n == 1 and m == 1: return 1
    if n < 1 or m < 1 : return 0


    return gridTraveler(n-1,m) + gridTraveler(n,m-1)

# memoized approach
# Time complexity -> O(n*m)
# Space complexity -> O(n*m)
    
def gridTraveler(n,m,memo={}):
    key = str(n) + ',' + str(m)
    if key in memo: return memo.get(key) 
    if n == 1 and m == 1: return 1
    if n < 1 or m < 1 : return 0


    memo[key] = gridTraveler(n-1,m,memo) + gridTraveler(n,m-1,memo)
    return memo.get(key)

    


print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
