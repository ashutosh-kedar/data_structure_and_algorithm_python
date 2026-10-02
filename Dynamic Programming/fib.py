
# brut forcr approach
# Time complexity -> O(2^n)
# Space complexity -> O(n)

def fib_brut(n):

    if n == 0 or n == 1: return 1

    return fib(n-2) + fib(n-1)

# memoized
# Time complexity -> O(n)
# Space complexity -> O(n) Space increases linearly as the memo is shared

def fib(n,memo={}):
    if n in memo.keys(): return memo.get(n)
    if n == 0 or n == 1: return 1

    memo[n] = fib(n-2) + fib(n-1)
    return memo[n]

print(fib(2))
print(fib(7))
print(fib(30))
print(fib(50))




## IMP
# Python's behaviour
# I forgot to pass memo in the recursive calls but its still fast, how?
# -> not passing memo doesn't create a new dictionary on every recursive call;
#    Python reuses the same default dictionary.


# For the same function: Python creates the default dictionary once when the function is defined. Every call that omits memo reuses that same dictionary, including recursive calls. Any values added to it remain there between calls, even after a call has finished, as long as the dictionary is still referenced.

# For another function: If another function has its own mutable default argument, it gets a separate dictionary.

# The dictionary persists as long as the function's default argument remains referenced. It isn't recreated on every call, nor is it necessarily deleted when a function finishes.


#That's why the recommended Python practice is to use None as the default and initialize the dictionary inside the function:

#This gives each independent call its own dictionary while still allowing recursive calls to share it when you explicitly pass memo.


