class Node():
    def __init__(self):
        self.neighbours = []
        self.colour = 0
        self.distance = -1  # the distance


class Graph():
    def __init__(self, n):
        self.nodes = [Node() for i in range(n)]

    def clear_graph(self):
        for node in self.nodes:
            node.distance = -1

    def connect(self, a, b):
        if a > len(self.nodes) or b > len(self.nodes):
            raise ValueError('Referencing to node that does not exist')
        self.nodes[a].neighbours.append(self.nodes[b])
        self.nodes[b].neighbours.append(self.nodes[a])

    def find_all_distances(self, s):  # s being index number directed at the graph
        queue = []
        self.nodes[s].distance = 0
        queue.append(self.nodes[s])
        while queue:
            current = queue.pop()
            current.color = 2
            for node in current.neighbours:
                if node.colour == 0:
                    queue.append(node)
                    node.distance = current.distance + 6
                    node.colour = 1
        resultstr = ''
        for index, node in enumerate(self.nodes):
            if index == s:
                continue
            resultstr = resultstr + str(node.distance) + ' '
        print (resultstr)
        self.clear_graph()

g= Graph(5)
for edge in [(0,1), (0,2), (0,4), (0,0),(2,4)]:
    g.connect(edge[0], edge[1])
g.find_all_distances(4)

