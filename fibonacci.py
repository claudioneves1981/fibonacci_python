def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memoization(n, memo):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

def fib_tabulation(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fib_two_variables(n):
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

fib_functions = {
    "Recursive": fib_recursive,
    "Memoization": lambda n: fib_memoization(n, {}),
    "Tabulation": fib_tabulation,
    "Two Variables": fib_two_variables
}

print("Fibonacci Sequence:")
for method, func in fib_functions.items():
    print(f"\nMethod: {method}")
    for i in range(1, 10):
        print(f"fib({i}) = {func(i)}")