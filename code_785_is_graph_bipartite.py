from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        seen = {}
        n = len(graph)
        def check(start):
            q = deque()
            q.append((start, 1))
            while q:
                node, color = q.popleft()
                if node in seen:
                    if seen[node] != color:
                        return False
                    continue
                seen[node] = color
                for v in graph[node]:
                    q.append((v, -color))
            return True

        for i in range(n):
            if i not in seen:
                if check(i) == False:
                    return False
        return True

        
