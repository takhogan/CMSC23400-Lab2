def find_distance(a, b, rss):
    AlogD = rss - b
    logD = AlogD / a
    d = 10**logD
    return d
