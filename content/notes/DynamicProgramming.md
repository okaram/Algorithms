# Dynamic Programming

* Many algorithms (Divide-and-conquer) involve solving smaller independent subproblems
* In DP problems you end up solving the *same* subproblems several times.
  * **Memoization** - Store solutions in a table when you produce them
  * **Dynamic programming** - Start from the apropriate small subproblems, build the table up

# Basic example: Fibbonacci sequence

**sequence** - 0 1 1 2 3 5 8, ... 

fib(0) = 0

fib(1) = 1

fib(n)=fib(n-1)+fib(n-2)

## python code
```python
def fibo(n:int)->int:
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
```

**problem** - we would solve the same problem many times (exponential)

## Memoization
One solution: **memoization**. We can do it manually. Create a table, insert values when we find them.

```python
fibo_table={0:0, 1:1}
def fibo_mm(n:int)->int:
  if n in fibo_table:
    return fibo_table[n]
  else:
    ans=fibo_mm(n-1)+fibo_mm(n-2)
    fibo_table[n]=ans
    return ans
```

* You could also pass the table as an argument to avoid globals.
* The table can be an array, a multivalued array, or a dictionary
* Try it - time this and the original fibo function with large-ish numbers, like 40 or 50.
* Hint - Python has a decorator that does this for you. Check functools.lru_cache

## Dynamic programming
Dynamic programming involves building from the bottom

```python
def fibo_dp(n:int)->int:
  table=[None]*n # array of size n
  table[0]=0
  table[1]=1
  for m in range(2,n):
    table[m]=table[m-1]+table[m-2]
  return table[n-1]+table[n-2]
```
* some times, you do not need to keep *all* the previous one.
* Homework - Redo fibo_dp keeping only the last two 

## More useful examples and problems

### Coin change

**problem** Give change with the least amount of coins. Notice greedy algorithm doesn't always work (depends on value of coins).

#### Recursive
```python
def recMC(coinValueList, target):
  minCoins = target # assume 1 is in coinValueList
  if target in coinValueList:
    return 1
  else:
    for i in [c for c in coinValueList if c <= target]:
      numCoins = 1 + recMC(coinValueList,target-i)
      if numCoins < minCoins:
        minCoins = numCoins
    return minCoins
```

#### Memoized (passing dictionary)

```python
def make_change_memo(coinValueList, target, knownResults):
  minCoins = target
  if target in coinValueList:
    knownResults[target] = 1
    return 1
  elif target in knownResults:
    return knownResults[target]
  else:
    for i in [c for c in coinValueList if c <= target]:
      numCoins = 1 + make_change_memo(coinValueList, target-i, knownResults)
      if numCoins < minCoins:
        minCoins = numCoins
    knownResults[target] = minCoins
    return minCoins
```

#### Dynamic programming
You can build a table with the minimum number of coins required for every number up to your target.

```python
def make_change_dp(coinValueList, target):
  minCoins = [None]*(target + 1)
  for cents in range(target+1):
    minCoins[cents] = cents
    for c in coinValueList:
      if cents >= c:
        minCoins[cents] = min(minCoins[cents], minCoins[cents - c] + 1)
  return minCoins[target]
```
### Edit distance (Levenshtein distance)
* Find the shortest edit distance between two strings. Allowed edits are (each one adds 1 to the distance):
  * Insert a blank on first string
  * Delete a character on first string
  * Replace character on first string with character in second


