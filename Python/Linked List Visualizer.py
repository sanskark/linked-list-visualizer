"""
This file contains
"""

from graphviz import Digraph
from graphviz import nohtml

if __name__ == "__main__":
    print("Enter a Linked List Nodes(Ex. 1 2 3 4 5): ")
    linked_list = [ele for ele in input().split()]

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

    # make a directed graph in DOT language and assigns attributes to it
    DOT = Digraph('Singly Linked List', node_attr=node_attr, graph_attr=graph_attr, edge_attr=edge_attr, format='png')

    # some custom DOT for edges initially empty
    custom_dot = ""

    prev_node = None    # previous node of the current node

    # iterate through input to make node and edges
    for node in linked_list:
        # if it is last node then assign next to NULL
        if node == linked_list[-1]:
            label = "{<data>" + node + "| <next> NULL}"
        else:
            label = "{<data>" + node + "|<next>}"

        # Make a node in DOT language
        DOT.node(node, nohtml(label))

        # Make an edge between nodes
        if prev_node is not None:
            custom_dot += f'\t{prev_node}:next:c->{node}\n'

        # assign prev_node to current node
        prev_node = node

    # appends the custom dot to body of DOT
    DOT.body.extend(custom_dot)

    DOT.render('../Outputs/linked_list.gv')
