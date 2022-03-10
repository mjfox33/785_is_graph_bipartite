from code_785_is_graph_bipartite import Solution

def test_example_1():
    s = Solution()
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    output = False
    assert s.isBipartite(graph) == output

def test_example_2():
    s = Solution()
    graph = [[1,3],[0,2],[1,3],[0,2]]
    output = True
    assert s.isBipartite(graph) == output
