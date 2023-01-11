class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, src):
            res = 0

            for child_node in graph[node]:
                if child_node != src:
                    res += dfs(child_node, node) #往子節點遞迴

            if (res or hasApple[node]) and src != -1: #遇到蘋果則可以開始進入步數，且可以帶著蘋果走回去原點
                return res + 2

            return res

        return dfs(0, -1)
