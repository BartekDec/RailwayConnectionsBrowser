from AbstractGraphInterface import IAbstractGraph


class WrongNodeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AdjacencyListGraph(IAbstractGraph):
    def __init__(self):
        self.adjacencyList = {}

    def addNode(self, node):
        if " " not in node:
            self.adjacencyList.update({node: []})
        else:
            raise Exception("more than one word")

    def addEdges(self, nodeName, args):
        args = args.split()
        if nodeName not in self.adjacencyList:
            raise WrongNodeError(nodeName)
        for i in args:
            self.adjacencyList[nodeName].append(i)

    def shortestPath(self, begin, end):
        if begin not in self.adjacencyList or end not in self.adjacencyList:
            raise WrongNodeError((begin, end))
        else:
            queue = [[begin]]
            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node == end:
                    if len(path) == 2:
                        info = "Direct connection"
                        return info, path
                    else:
                        info = "Connection with change"
                        return info, path
                for adjacency in self.adjacencyList.get(node, []):
                    newPath = list(path)
                    newPath.append(adjacency)
                    queue.append(newPath)

    def displayGraph(self):
        return self.adjacencyList

    def removeNode(self, node):
        del self.adjacencyList[node]

    def removeConnection(self, nodeName, args):

        args = args.split()
        for i in args:
            self.adjacencyList[nodeName].remove(i)





