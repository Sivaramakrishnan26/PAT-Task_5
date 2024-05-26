from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(0, n - 2), [0, 1])
print(fibonacci(50))  # Print the output
