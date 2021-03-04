
b = [p[0] for p in sorted([(i, sum(j)) for i, j in enumerate(mat)], key=lambda a: a[1])[:k]]
