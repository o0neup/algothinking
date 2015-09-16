# coding: utf-8
"""
Created on: 2015-09-15
author: 'artemkorkhov'
"""

import urllib2
import math
import matplotlib.pyplot as plt

from .project_1 import in_degree_distribution


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
    graph_lines = graph_lines[ : -1]

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
    x = [math.log(key) for key in degree_distr.keys() if key != 0]
    y = [math.log(val) for val in degree_distr.values() if val !=0]
    if len(x) != len(y):
        y = y[1:]

    return plt.plot(x, y, 'ro')


def er_directed(num_nodes, prob):
    """ Generates directed Erdos-Renyi graph
    :param num_nodes:
    :param prob:
    :return:
    """
    raise NotImplementedError



