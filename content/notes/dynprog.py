
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

