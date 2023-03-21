from random import randint

class Graph():
    def __init__(self) -> None:
        self._edges = {}

    def _add_vertex(self, from_vert: int, to_vert: int = None, cost: int = None):
        if not self._edges.get(from_vert):
            self._edges[from_vert] = {}

        if to_vert is not None:
            self._edges[from_vert][to_vert] = cost

    def add_vertex(self, from_vert: int, to_vert: int = None, cost: int = None):
        self._add_vertex(from_vert, to_vert, cost)
        if to_vert is not None:
            self._add_vertex(to_vert, from_vert, cost)

    def add_vertex_oneway(self, from_vert: int, to_vert: int = None, cost: int = None):
        self._add_vertex(from_vert, to_vert, cost)

    def get(self, val) -> dict:
        return self._edges.get(val, {})

    def get_all_vertex(self):
        return [j for j in self._edges]

    def get_all_vertex_flatten(self):
        temp = []
        for k, v in self._edges.items():
            for i in v:
                if i not in temp:
                    temp.append(i)
            if k not in temp:
                temp.append(k)

        return temp

    def __str__(self) -> str:
        string = ""
        for i in self._edges:
            string += f"{i} - "
            for j in self._edges[i]:
                string += f"{j}, "
            string = string[:-2] + "\n"

        return string

    def __repr__(self) -> str:
        return self.__str__()

def generate_edges(graph: Graph):
    for _ in range(0, 10):
        x = y = 0
        while x == y:
            x = randint(0,5)
            y = randint(0,5)
        graph.add_vertex(x, y)

    graph.add_vertex(6, None)

def find_isolated_nodes(graph: Graph):
    isolated = []
    verticies = graph.get_all_vertex()
    for i in verticies:
        if not graph.get(i):
            isolated.append(i)

    return isolated


def find_path(start: int, end: int, path:list, graph: Graph):
    path.append(start)
    re = None
    if start == end:
        return 0

    for i in graph.get(start):
        if i in path:
            continue
        re = find_path(i, end, path, graph)
        if re == 0:
            return 0

    if re == None:
        path.pop()

def find_all_paths(start: int, end: int, path:list, graph: Graph, walked = None):
    if walked is None:
        walked = []
    walked.append(start)

    if start == end:
        path.append(walked.copy())
        walked.pop()
        return

    for i in graph.get(start):
        if i in walked:
            continue
        find_all_paths(i, end, path, graph, walked)
    walked.pop()

def is_connected(vert_encountered: list = None, start:int = None, graph: Graph = None):
    if start in vert_encountered:
        return

    vert_encountered.append(start)
    for i in graph.get(start):
        is_connected(vert_encountered, i, graph)

#
g1 = Graph()
g2 = Graph()
generate_edges(g1)
generate_edges(g2)
print(g1)
print(g2)

print("\nisolation")

isolation1 = find_isolated_nodes(g1)
isolation2 = find_isolated_nodes(g2)
print(isolation1)
print(isolation2)

print("\nfind single path")
p1 = []
p2 = []
find_path(5, 0, p1, g1)
find_path(5, 0, p2, g2)
print(p1)
print(p2)

print("\nfind all paths")
p1all = []
p2all = []
find_all_paths(0, 3, p1all, g1)
find_all_paths(0, 3, p2all, g2)
print(p1all)
print(p2all)

print("\nfind connected")
pconnect1 = []
pconnect2 = []
is_connected(pconnect1, 0, g1)
is_connected(pconnect2, 0, g2)
print(pconnect1)
print(pconnect2)

def generate_graph_excer2(graph: Graph):
    graph.add_vertex_oneway("A", "B")
    graph.add_vertex_oneway("A", "C")
    graph.add_vertex_oneway("A", "F")
    graph.add_vertex_oneway("B", "A")
    graph.add_vertex_oneway("B", "D")
    graph.add_vertex_oneway("B", "E")
    graph.add_vertex_oneway("C", "B")
    graph.add_vertex_oneway("C", "F")
    graph.add_vertex_oneway("D", "A")
    graph.add_vertex_oneway("D", "E")
    graph.add_vertex_oneway("D", "F")
    graph.add_vertex_oneway("E", "A")
    graph.add_vertex_oneway("E", "D")

def generate_val_graph(graph: Graph):
    graph.add_vertex_oneway(1, 2, 10)
    graph.add_vertex_oneway(0, 10, 10)
    graph.add_vertex_oneway(1, 3, 15)
    graph.add_vertex_oneway(1, 6, 5)
    graph.add_vertex_oneway(2, 3, 7)
    graph.add_vertex_oneway(3, 4, 7)
    graph.add_vertex_oneway(3, 6, 10)
    graph.add_vertex_oneway(4, 5, 7)
    graph.add_vertex_oneway(6, 4, 5)
    graph.add_vertex_oneway(5, 6, 13)

def BFS(start, graph: Graph,path: list = None):
    q = [start]
    visited = [start]
    while q:
        i = q.pop()
        path.append(i)

        for j in graph.get(i):
            if j not in visited:
                q.append(j)
                visited.append(j)

def DFS(start, graph: Graph, path:list = None):
    s = [start]
    while s:
        i = s.pop()
        if i not in path:
            path.append(i)
            s.extend(graph.get(i).keys() - path)

def dijkstra(start, graph: Graph):
    distance = {}
    visitnt = []
    for i in graph.get_all_vertex_flatten():
        visitnt.append(i)
        if i == start:
            distance[i] = {"path": [start], "cost": 0}
        else:
            distance[i] = {"path": [start], "cost": float("inf")}
    walked = []
    current_path = start
    while visitnt:
        smallest = current_path
        current_cost = distance[current_path]["cost"]
        walked.append(current_path)
        for path, cost in graph.get(current_path).items():
            if path in visitnt and distance[path]["cost"] >= cost + current_cost:
                walked.append(path)
                smallest = path
                distance[path]["cost"] = cost + current_cost
                distance[path]["path"] = walked.copy()
                walked.pop()

        visitnt.remove(current_path)

        if smallest == current_path and visitnt:
            current_path = visitnt[0]
            walked = distance[current_path]["path"][:-1]
        else:
            current_path = smallest

    return distance

def print_dijstra_pretty(d: dict):
    string = ""
    for v in d.values():
        for i in v['path']:
            string += str(i) + " -> "
        string = string[:-4] + f" : {v['cost']}\n"

    print(string)

gbfs = Graph()
pbfs = []
print('\nBFS')
generate_graph_excer2(gbfs)
BFS("A", gbfs, pbfs)
print(pbfs)

gcost = Graph()
pcost = []
generate_val_graph(gcost)
print("\nDFS")
DFS(1, gcost, pcost)
print(pcost)

gdij = Graph()
generate_val_graph(gdij)
print("\nDijkstra")
print(gdij)
distance = dijkstra(1, gdij)
print_dijstra_pretty(distance)
