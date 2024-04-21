# adapted from https://book.acmicpc.net/ds/segment-tree

import sys

input = sys.stdin.readline


class BinarySegmentTree:
    def __init__(self, arr_len):
        tree_height = 2
        tmp = arr_len - 1
        while tmp := tmp >> 1:
            tree_height += 1
        self.arr_len = arr_len
        self.tree_height = tree_height
        self._qinit = []
        self._qop = []
        self.qdata = []

    def register(self, q_operator, q_init):
        self._qop += [q_operator]
        self._qinit += [q_init]
        self.qdata += [[q_init] * 2 ** self.tree_height]
        return len(self._qop) - 1

    def initialize_value(self, arr_init, qtype):
        assert len(arr_init) <= self.arr_len
        self._initialize_value(arr_init, 1, 0, len(arr_init) - 1, qtype)

    def _initialize_value(self, a, node, start, end, qtype):
        """initialize node=op(a[start~end]) (start & end inclusive)"""
        if start == end:
            self.qdata[qtype][node] = a[start]
        else:
            self._initialize_value(a, node * 2, start, (start + end) // 2, qtype)
            self._initialize_value(a, node * 2 + 1, (start + end) // 2 + 1, end, qtype)
            self.qdata[qtype][node] = self._qop[qtype](self.qdata[qtype][node * 2], self.qdata[qtype][node * 2 + 1])

    def query(self, left, right, qtype):
        """get val=op(a[left~right]) (left & right inclusive)"""
        return self._query(1, 0, self.arr_len - 1, left, right, qtype)

    def _query(self, node, start, end, left, right, qtype):
        if left > end or right < start:
            return self._qinit[qtype]
        if left <= start and end <= right:
            return self.qdata[qtype][node]
        lq = self._query(node * 2, start, (start + end) // 2, left, right, qtype)
        rq = self._query(node * 2 + 1, (start + end) // 2 + 1, end, left, right, qtype)
        return self._qop[qtype](lq, rq)


if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        arr += [int(input())]

    from operator import add

    segmenttree = BinarySegmentTree(len(arr))
    minquery = segmenttree.register(min, float('inf'))
    maxquery = segmenttree.register(max, -float('inf'))
    sumquery = segmenttree.register(add, 0)
    segmenttree.initialize_value(arr, minquery)
    segmenttree.initialize_value(arr, maxquery)
    segmenttree.initialize_value(arr, sumquery)


    for i in range(m):
        b, c = map(int, input().split())
        o1 = segmenttree.query(b - 1, c - 1, minquery)
        o2 = segmenttree.query(b - 1, c - 1, maxquery)
        o3 = segmenttree.query(b - 1, c - 1, sumquery)
        print(o1, o2, o3)
