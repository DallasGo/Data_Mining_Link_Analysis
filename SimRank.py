#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:03:07 2018

@author: charline
"""
import collections
import copy
import operator
from pygraph.classes.digraph import digraph


def simrank(G, c=0.6, max_iter=100):
    
    temp_sim = collections.defaultdict(list)
  
    sim = collections.defaultdict(list)
    for n in G.nodes():
        sim[n] = collections.defaultdict(int)
        sim[n][n] = 1
        temp_sim[n] = collections.defaultdict(int)
        temp_sim[n][n] = 0
      
    for iter_ctr in range(max_iter):
        if isConverge(sim, temp_sim):
            break
        temp_sim = copy.deepcopy(sim)
        for a in G.nodes():
            for b in G.nodes():
                num = len(list(G.incidents(a))) * len(list(G.incidents(b)))
                #print(num)
                if a == b:
                    continue
                elif num==0:
                    sim[a][b] =0.0
                s_ab = 0.0
                #print(num)
                for n_a in G.incidents(a):
                    #print(num)
                    for n_b in G.incidents(b):
                        s_ab += temp_sim[n_a][n_b]
                        #print(s_ab)
                    #if num==0:
                        #sim[a][b]=1
                        #print(sim[a][b])
                    #else:
                        sim[a][b] = (c * s_ab / (len(list(G.incidents(a))) * len(list(G.incidents(b)))))
                        #print(num)
    return sim

def isConverge(s1, s2):
  if s1 != s2:
      return False
  return True



file = open('./Dataset/graph_1.txt')

G = digraph()
nodes = []
myline = []
for line in file:
    line = line.strip().split(",")
    myline.append(line)
    for node in line:
        nodes.append(node)
nodes = set(nodes)
nodes = sorted(nodes, key=lambda x: int(x[0])) 

G.add_nodes(nodes)
for i in myline:
    G.add_edge(i)

sim = simrank(G)
for i in sorted(sim, key=operator.itemgetter(0)):
    print(i,dict(sim[i]))
