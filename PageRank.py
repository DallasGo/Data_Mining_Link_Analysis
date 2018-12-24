#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:22:08 2018

@author: charline
"""

from pygraph.classes.digraph import digraph
import operator

def page_rank(G,damping_factor,max_iterations, min_delta):
    nodes = G.nodes()
    graph_size = len(nodes)
    
    if graph_size == 0:
        return {}
    page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  
    #print(page_rank)
    damping_value = (damping_factor) / graph_size 
    
    for i in range(max_iterations):
        change = 0
        for node in nodes:
            rank = 0
            for par_node in G.incidents(node):  
                rank += (page_rank[par_node] / len(G.neighbors(par_node))) 
            rank = (1-damping_factor) * rank
            rank += damping_value
            change += abs(page_rank[node] - rank)
            page_rank[node] = rank
    
        if change < min_delta:
            break
    
    return page_rank

#==============================================  
file = open('./Dataset/kaggle_out.txt')
G = digraph()
nodes = []
myline = []
for line in file:
    line = line.strip().split(",")
    for node in line:
        if "NONE" == node.strip():
            line.remove(node)
    if(len(line) > 1):
        #print (line)
        if len(line)>2:
            for k in range(0,len(line)-1):
                newline = []
                newline.append(line[k].strip())
                newline.append(line[k+1].strip())
                #print (i[k])
                myline.append(newline)
                #print (newline)
                #print(line[k].strip())
        else:
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            #print (line)
            myline.append(line)
        #print (line)
        for node in line:
            nodes.append(node.strip())
#print(myline)
nodes = set(nodes)
#nodes = sorted(nodes, key=lambda x: int(x[0])) 
#print(nodes)

G.add_nodes(nodes)

for i in myline:
    if G.has_edge(i):
        continue
    else: G.add_edge(i)    
#==============================================    
'''
file = open('./Dataset/graph_6.txt')

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

#G.del_edge(('3','4'))
#G.del_edge(('2','3'))

'''
damping_factor = 0.15  
max_iterations = 1000  
min_delta = 0.00001

page_ranks = page_rank(G,damping_factor,max_iterations, min_delta)

page_ranks = sorted(page_ranks.items(), key=operator.itemgetter(1),reverse=True)

print("The page rank is\n", page_ranks)

      