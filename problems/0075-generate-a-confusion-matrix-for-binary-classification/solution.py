
from collections import Counter

def confusion_matrix(data):
    # Implement the function here
    counts = Counter(tuple(pair) for pair in data)
    tp = counts[(1, 1)]
    fn = counts[(1, 0)]
    fp = counts[(0, 1)]
    tn = counts[(0, 0)]

    return [[tp, fn], [fp, tn]]
    pass
