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

### python code
```{.py}
def fibo(n:int)->int:
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
```



