class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        res = [0 for i in range(len(labels))]
        count = collections.defaultdict(int) #計算標籤出現次數

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, src):
            tmp = count[labels[node]] #將其祖先節點的標籤次數先存起來
            count[labels[node]] += 1

            for child_node in graph[node]:
                if child_node != src:
                    dfs(child_node, node)

            res[node] = count[labels[node]] - tmp #扣掉祖先節點的標籤次數

        dfs(0, -1)
            
        return res
