# Upsolving prob G with editorial
# https://atcoder.jp/contests/abc284/editorial/5491

"""Editorial Summary

let AA = cartesian_product(range(n), n)  i.e. Z_n ^n
o = sum_AA sum_{i in range(n)} S_i
  = sum_{i in range(n)} sum_AA S_i
  = n sum_AA S_0  ... (1)
(1) Because, let C_i be the number of As in AA with A_0=i.
    Then C_i=C_j for i,j in range(n).
    Therefore, WLOG, consider we always start from the node 0, and multiply by n.
Consider A's where the number of nodes reachable from node 0 is l.
* First pick l-1 nodes that should be reachable by 0. -> (n-1)C(l-1) cases
* The first l-1 nodes should be directed sequentially,
  making a permutation D with these nodes, starting from 0. -> (l-1)! cases
* And the remaining nodes should direct to any nodes. -> n^(n-l) cases
* The last node of the permutation should direct within the nodes that are reachable by 0.
  the direction of the last node determines S_0.
  S_0 = 0,1,...,l-1 for every 1 cases.
Therefore, o = n * sum_{l=1,...,n}{(n-1)C(l-1) * (l-1)! * n^(n-l) * (sum{i=0 ... l-1} i)}
             = n * sum_{l=1,...,n}{(n-1)P(l-1) * n^(n-l) * l*(l-1) / 2}
"""

# careful! m may not be prime. (no mod inverse)
n, m = map(int, input().split())

c = 1
prepow = []
for i in range(n):
    prepow += [c]
    c = c * n % m

o = 0
perm = 1
for l in range(1, n + 1):
    o += perm * prepow[n - l] * (l * (l - 1) // 2) % m
    perm = perm * (n - l) % m
o = o * n % m
print(o)
