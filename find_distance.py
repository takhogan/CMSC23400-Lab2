def find_distance(a, b, rss):
    AlogD = rss - b
    logD = AlogD / a
    d = 10**logD
    return d

print(find_distance(4, 2, 14))
