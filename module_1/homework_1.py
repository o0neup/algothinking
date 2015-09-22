# coding: utf-8
"""
Created on: 2015-09-15
author: 'artemkorkhov'
"""
import copy
import urllib2
import random
import matplotlib.pyplot as plt

from project_1 import in_degree_distribution, make_complete_graph, compute_in_degrees


CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def get_normalized_in_degree_distr(graph):
    """
    :param graph:
    :return:
    """
    size = len(graph.keys())
    degree_distr = in_degree_distribution(graph)

    normalized = {}
    for degree in degree_distr:
        normalized[degree] = degree_distr[degree]/float(size)
    return normalized


def plot_degree_distr(degree_distr):
    """
    :param degree_distr:
    :return:
    """
    x = [key for key in degree_distr.keys() if key != 0]
    y = [val for val in degree_distr.values() if val !=0]
    if len(x) != len(y):
        y = y[1:]

    _plot = plt.plot(x, y, 'ro')
    plt.xlabel("in-degree of node")
    plt.ylabel("normalized distribution")
    plt.xscale("log")
    plt.yscale("log")
    return _plot


def er_directed(num_nodes, prob):
    """ Generates directed Erdos-Renyi graph
    :param num_nodes:
    :param prob:
    :return:
    """
    graph = {node: set() for node in xrange(num_nodes)}
    for node in xrange(num_nodes):
        for other_node in xrange(num_nodes):
            if prob > random.random() and node != other_node:
                graph[node].add(other_node)
    return graph


def dpa(n, m):
    """
    :param n:
    :param m:
    :return:
    """
    assert 1 <= m <= n
    graph = make_complete_graph(m)
    in_degrees = compute_in_degrees(graph)
    for i in range(m, n):
        nodes = set()
        vertices = set(copy.copy(graph.keys()))
        for _ in range(m):
            new_vert = random.choice(list(vertices))
            vertices.remove(new_vert)
            nodes.add(new_vert)
        graph.update({i: nodes})
        print "done with node %s" % i
    return graph


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors






