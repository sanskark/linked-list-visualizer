"""

"""

from graphviz import Digraph
from graphviz import nohtml

print("Enter a Linked List Nodes(Ex. 1 2 3 4 5): ")
user_input = [ele for ele in input().split()]

# graph attributes
graph_attr = {
    'rankdir': 'LR'
}

# node attributes
node_attr = {
    'shape': 'record',
    'fontname': 'Consolas',
    'width': '1.3',
    'height': '.5'
}

# edge attributes
edge_attr = {
    'arrowhead': 'vee',
    'arrowtail': 'dot',
    'tailclip': 'false',
    'dir': 'both'
}

