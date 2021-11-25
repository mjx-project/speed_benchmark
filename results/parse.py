import sys
import numpy as np

tsv = sys.argv[1]


def parse(x):
    m = float(x.split("m")[0])
    s = float(x.split("m")[1].split("s")[0].strip())
    return 60 * m + s


mjx = []
mjai = []

with open(tsv, "r") as f:
    for line in f:
        x, y = line.split("\t")
        x, y = parse(x), parse(y)
        mjx.append(x)
        mjai.append(y)

print("mjx = ", mjx)
print(np.mean(mjx), np.std(mjx))
print("mjai = ", mjai)
print(np.mean(mjai), np.std(mjai))
