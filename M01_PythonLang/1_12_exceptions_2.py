def divide(x: int, y: int):
    return x // y

m = divide(10, 0)
print(m)

# line A calls line B, line B calls line C
# Call stack:  ~ Python Traceback 
# -- A (line 4)
#  -- B (line 2)
#   -- C

# Return stack: (also applicable to exception raising)
#   -- C
#  -- B
# -- A

# f(x) = x + 1
# f(x^2 + 1) = f(g(x)) with g(x) = x^2 + 1
