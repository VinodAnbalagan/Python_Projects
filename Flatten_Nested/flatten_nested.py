def flatten(L):
    for e in L:
        if hasattr(e, '__iter__'):
            yield from flatten(e)
        else:
            yield e


# Test
f = flatten([1, 2, [3, 4, 5], 6, [7, 8, 9], 10, [11, 12, 13], 14, 15])
result = list(f)
print(result)
