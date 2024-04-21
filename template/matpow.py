# adapted from pyrival

mod = 1_000_007
mat_add = lambda *mat: [[sum(elements)%mod for elements in zip(*row)] for row in zip(*mat)]
mat_mul = lambda A, B: [[sum(i * j % mod for i, j in zip(row, col))%mod for col in zip(*B)] for row in A]


def eye(m):
    """returns an identity matrix of order m"""
    identity = [[0] * m for _ in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1
    return identity


def mat_pow(mat, power):
    """returns mat**power"""
    assert power>=0  # inverse not supported

    result = eye(len(mat))
    if power == 0:
        return result

    while power > 1:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1
    return mat_mul(result, mat)