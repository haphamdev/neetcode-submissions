class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def root(n1) -> int:
            res = n1
            while res != parents[res]: res = parents[res]
            return res
        
        def union(n1, n2) -> int:
            p1, p2 = root(n1), root(n2)
            
            if p1 == p2: return 0

            if ranks[p1] < ranks[p2]:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            else:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res