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
print(f"{np.mean(mjx):.03f} {np.std(mjx):.03f}" )
print("mjai = ", mjai)
print(f"{np.mean(mjai):.03f} {np.std(mjai):.03f}" )
