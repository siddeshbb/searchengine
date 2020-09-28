"""
Graph module.
"""

class Graph(object):
    """
    Represents a directed graph.
    """

    def __init__(self):
        """
        Initializes the Graph to an empty graph with no nodes or edges.
        """
        self.graph = {}
        
    def add_node(self, node):
        """
        If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
        """
        if node in self.graph:
            return False
        else:
            self.graph[node] = []
            return True

    def has_node(self, node):
        """
        Returns True if node is a node in the graph.
        """
        if node in self.graph:
            return True
        else:
            return False


    def add_edge(self, node1, node2):
        """
        Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
            

    def get_nodes(self):
        """
        Returns a frozenset containing the nodes in the graph.
        """
        nodes = set()
        for node in self.graph:
            nodes.add(node)
        return frozenset(nodes)

    def get_outlinks(self, node):
        """
        Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
        """
        if node not in self.graph:
            return None
        return frozenset( self.graph[node] )

    def get_inlinks(self, target):
        """
        Requires: node is a node in self.
        Returns a set of the nodes that are connected by an edge to node.
        """
        nodes = set()
        if target not in self.graph:
            return None
        for node in self.graph:
            if target in self.graph[node]:
                nodes.add(node)
        return frozenset(nodes)
    
    def __str__(self):
        """
        Returns a string representation of the graph. 
        """
        stringgraph = ''
        for node in self.graph:
            stringgraph = stringgraph + node
            stringgraph = stringgraph + ' -> '
            stringgraph = stringgraph + str(self.graph[node])
            stringgraph = stringgraph + '\n'
        return stringgraph
