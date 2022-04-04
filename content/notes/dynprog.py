
def fibo(n:int)->int:
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

# manually memoizing
fibo_table={0:0, 1:1}
def fibo_mm(n:int)->int:
  if n in fibo_table:
    return fibo_table[n]
  else:
    ans=fibo_mm(n-1)+fibo_mm(n-2)
    fibo_table[n]=ans
    return ans

import functools

@functools.lru_cache
def fibo_memo(n:int)->int:
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo_memo(n-1)+fibo_memo(n-2)

def fibo_dp(n:int)->int:
  table=[None]*n # array of size n
  table[0]=0
  table[1]=1
  for m in range(2,n):
    table[m]=table[m-1]+table[m-2]
  return table[n-1]+table[n-2]

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

def make_change_dp(coinValueList, target):
  minCoins = [None]*(target + 1)
  for cents in range(target+1):
    minCoins[cents] = cents
    for c in coinValueList:
      if cents >= c:
        minCoins[cents] = min(minCoins[cents], minCoins[cents - c] + 1)
  return minCoins[target]

print(make_change_memo([1,5,10,25],63, {}))
print(make_change_dp([1,5,10,25],1))