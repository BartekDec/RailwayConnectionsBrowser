class IAbstractGraph:
    """Graph Interface"""
    def addNode(self, node):
        raise NotImplementedError("Not Implemented Method")

    def addEdges(self, nodeName, args):
        raise NotImplementedError("Not Implemented Method")

    def shortestPath(self, begin, end):
        raise NotImplementedError("Not Implemented Method")

    def displayGraph(self):
        raise NotImplementedError("Not Implemented Method")

    def removeNode(self, node):
        raise NotImplementedError("Not Implemented Method")

    def removeConnection(self, begin, end):
        raise NotImplementedError("Not Implemented Method")
