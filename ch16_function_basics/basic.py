def times(x, y):
    return x * y

print(times(2, 3))

def intersect(seq1, seq2):
    return [x for x in seq1 if x in seq2]

print(intersect('SPAM', 'SCAM'))