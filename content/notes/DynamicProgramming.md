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
* Try it - time this and the original fibo function with large-ish numbers, like 40 or 50.

* Hint - Python has a decorator that does this for you. Check functools.lru_cache

## Dynamic programming
Dynamic programming involves building from the bottom

```python
def fibo_dp(n:int)->int:
  f=[None]*n # array of size n
  f[0]=0
  f[1]=1
  for m in range(2,n):
    f[m]=f[m-1]+f[m-2]
  return f[n-1]+f[n-2]
```

# More useful examples and problems


