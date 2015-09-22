# coding: utf-8
"""
Created on: 2015-09-15
author: 'artemkorkhov'

Sig! all extensive set notation made in complience with OwlTest (Coursera grading mechanism for this course)
"""

from collections import Counter


EX_GRAPH0 = {
    0: set([1, 2]),
    1: set([]),
    2: set([])
}


EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}


EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7])
}


def make_complete_graph(num_nodes):
    """ returns complete graph
    :param num_nodes: number of nodes in the graph
    :return dict graph:
    """
    if not isinstance(num_nodes, int):
        raise ValueError("num_nodes must be int!")
    if num_nodes <= 0:
        return {}

    graph = {}
    nodes = set(range(num_nodes))
    for node in nodes:
        graph.update({
            node: nodes.difference(set([node]))
        })
    return graph


def compute_in_degrees(digraph):
    """ Computes in-degree for each node of the graph
    :param digraph:
    :return:
    """
    if not isinstance(digraph, dict):
        raise ValueError("digraph must be dict!")
    in_degrees = {}
    for node in digraph:
        in_degrees.setdefault(node, 0)
        for other_node in digraph:
            if node == other_node:
                continue
            else:
                if node in digraph[other_node]:
                    in_degrees[node] += 1
        if node % 1000 == 0:
            print "computed %s nodes" % node
    return in_degrees


def in_degree_distribution(digraph):
    """ Computes non-normalized in-degree distribution
    :param digraph:
    :return:
    """
    in_degrees = compute_in_degrees(digraph)
    return dict(Counter(in_degrees.values()))

