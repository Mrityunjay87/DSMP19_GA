
#Python Mini Challenge
from itertools import groupby
def compress(s):
    s=s.lower()
    groups = groupby(s)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    return "".join("{}{}".format(label, count) for label, count in result)
