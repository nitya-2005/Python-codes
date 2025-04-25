import math

def calculate_ncr(n, r):
    return math.comb(n, r)

def calculate_npr(n, r):
    return math.perm(n, r)


n = 5
r = 3

ncr = calculate_ncr(n, r)
npr = calculate_npr(n, r)

print(f"{n} choose {r} (nCr) = {ncr}")
print(f"{n} permute {r} (nPr) = {npr}")

