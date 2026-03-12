class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b: return False

            if rank[a] < rank[b]:
                root[a] = b
            elif rank[b] < rank[a]:
                root[b] = a
            else:
                root[b] = a
                rank[a] += 1
            
            return True

        required = []
        optional = []
        for e in edges:
            if e[-1]:
                required.append(e)
            else:
                optional.append(e)

        strength = inf
        for u, v, s, m in required:
            if not union(u, v):
                return -1
            strength = min(strength, s)
            n -= 1
            
        optional.sort(key=lambda e: -e[2])
        
        for u, v, s, _ in optional:
            if union(u, v):
                n -= 1
                if n <= k: 
                    strength = min(strength, 2 * s)
                else:
                    strength = min(strength, s)
        
        return strength if n == 1 else - 1
