
# class union-find
class UF:
    def __init__(self, nv):
        self.nv = nv
        self.gparent = list(range(nv))
        self.grank = [0]*nv
        self.gsize = [1]*nv


    def find(self, x):
        # returns root node. with path compression
        if self.gparent[x] != x:
            self.gparent[x] = self.find(self.gparent[x])
        return self.gparent[x]


    def union(self, x, y):
        # union by rank.
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry:
            return rx
        sx = self.grank[rx]
        sy = self.grank[ry]
        # merge small rank into large rank.
        if sx > sy:
            ry, rx = rx, ry
        elif sx < sy:
            pass
        else:
            self.grank[ry] += 1
        # rx merge into ry
        self.gparent[rx] = ry
        self.gsize[ry] += self.gsize[rx]
        self.gsize[rx] = 0
        return ry
# end class


if __name__ == '__main__':
    nv = 100000
    uf = UF(nv)
    # root node traverse example
    for i in range(nv):
        if uf.gparent[i] == i:
            pass
