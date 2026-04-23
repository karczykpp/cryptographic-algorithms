import numpy as np

# L1  = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L1 = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
L2 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# L3  = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
L3 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
L4 = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L5 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
L6 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
L7 = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
L8 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
L9 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
L10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

L = np.array([L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])

ITERATIONS = 100


def getM(L):
    M = np.zeros([10, 10], dtype=float)
    # number of outgoing links
    c = np.zeros([10], dtype=int)

    for i in range(10):
        c[i] = np.sum(L[i])

    for i in range(10):
        for j in range(10):
            if L[i][j] == 1 and c[i] > 0:
                M[j][i] = 1 / c[i]

    return M


print("Matrix L (indices)")
print(L)

M = getM(L)

print("Matrix M (stochastic matrix)")
print(M)

### TODO 2: compute pagerank with damping factor q = 0.15
### Then, sort and print: (page index (first index = 1 add +1) : pagerank)
### (use regular array + sort method + lambda function)
print("PAGERANK")

q = 0.15
n = 10

pr = np.ones([10], dtype=float) / 10

for _ in range(ITERATIONS):
    new_pr = np.zeros([10], dtype=float)
    for i in range(n):
        suma = 0.0
        for j in range(n):
            suma += M[i][j] * pr[j]
        new_pr[i] = (q / n) + (1 - q) * suma
    pr = new_pr

pr_sorted = sorted([(i+1, pr[i]) for i in range(10)], key=lambda x: x[1], reverse=True)
for idx, val in pr_sorted:
    print(f"Strona {idx}: {val:.4f}")

### TODO 3: compute trustrank with damping factor q = 0.15
### Documents that are good = 1, 2 (indexes = 0, 1)
### Then, sort and print: (page index (first index = 1, add +1) : trustrank)
### (use regular array + sort method + lambda function)
print("TRUSTRANK (DOCUMENTS 1 AND 2 ARE GOOD)")

q = 0.15

d = np.zeros([10], dtype=float)
d[0] = 1.0
d[1] = 1.0

d = d / np.sum(d)

tr = np.copy(d)

for _ in range(ITERATIONS):
    tr = q * d + (1 - q) * np.dot(M, tr)

tr_sorted = sorted([(i+1, tr[i]) for i in range(10)], key=lambda x: x[1], reverse=True)
for idx, val in tr_sorted:
    print(f"Strona {idx}: {val:.4f}")





tr = [v for v in d]
print("TRUSTRANK MODIFICATED ")

### TODO 4: Repeat TODO 3 but remove the connections 3->7 and 1->5 (indexes: 2->6, 0->4)
L_mod = np.copy(L)

L_mod[2, 6] = 0
L_mod[0, 4] = 0

M_mod = getM(L_mod)

tr_mod = np.copy(d)
for _ in range(ITERATIONS):
    tr_mod = q * d + (1 - q) * np.dot(M_mod, tr_mod)

tr_mod_sorted = sorted([(i+1, tr_mod[i]) for i in range(10)], key=lambda x: x[1], reverse=True)
for idx, val in tr_mod_sorted:
    print(f"Strona {idx}: {val:.4f}")
### before computing trustrank
