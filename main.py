from collections import deque
from heapq import heappush, heappop
import heapq
from queue import PriorityQueue 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    pq = []
    visited = set()
    heappush(pq, (source,0,0))
    res = dict()
    layer = 0
    queue = deque()
    queue.append((source, 0, 0))
    seen = set()
    a = graph[source].copy()
    graph[source].clear()
    
    for node, weight in a:
      graph[source].add((node, weight, 1))
    #print(graph)

    while queue:
      node, weight, layer = queue.popleft()
      if node in seen:
        continue
      seen.add(node)
      nodes = graph[node].copy()
      if layer != 0:
        graph[node].clear()
        for children, weight in nodes:
          newnode = (children, weight, layer+1)
          queue.append(newnode)
          graph[node].add(newnode)
      else:
        for children, weight, layer in nodes:
          newnode = (children, weight, layer)
          queue.append(newnode)

    #print(graph)
    while pq:
      node, weight, layer = heappop(pq)
      if node in visited:
        continue
      visited.add(node)
      res[node] = (weight, layer)

      for children, newweight, layer in graph[node]:
        heappush(pq, (children, weight + newweight, layer))

    return res
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    print(result)
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
test_shortest_shortest_path()
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    queue = deque()
    queue.append((source, 'none'))
    visited = set()
    res = dict()
    while queue:
      node = queue.popleft()
      if node[0] in visited:
        continue
      visited.add(node[0])
      res[node[0]] = node[1]
      for children in graph[node[0]]:
        queue.append((children, node[0]))

    res.pop(source)
    return res
    
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    print(parents)
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'

test_bfs_path()
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    res = ''
    while destination in parents:
      res += parents[destination]
      destination = parents[destination]

    return res[::-1]

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    print(get_path(parents, 'd'))
    assert get_path(parents, 'd') == 'sbc'

test_get_path()
