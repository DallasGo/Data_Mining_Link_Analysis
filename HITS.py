#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:25:31 2018

@author: charline
"""

from pygraph.classes.digraph import digraph
import math
import operator
import networkx as nx


def HITS(G,max_iterations,min_delta):
    authority = {} 
    hub = {}
    for node in G.nodes():
        hub[node] = 1
        authority[node] = 1
    for i in range(max_iterations):
        change = 0.0  
        norm = 0  
        tmp = {}
        # authority===============================
        tmp = authority.copy()
        
        for node in G.nodes():
            authority[node] = 0
            for pa_node in G.incidents(node):  
                authority[node] += hub[pa_node]
            norm += pow(authority[node], 2)
        # normalization
        norm = math.sqrt(norm)
        for node in G.nodes():
            authority[node] /= norm
            change += abs(tmp[node] - authority[node])
    
        # hub===============================
        norm = 0
        tmp = hub.copy()
        for node in G.nodes():
            hub[node] = 0
            for ch_node in G.neighbors(node):
                hub[node] += authority[ch_node]
            norm += pow(hub[node], 2)
        # normalization
        norm = math.sqrt(norm)
        for node in G.nodes():
            hub[node] /= norm
            change += abs(tmp[node] - hub[node])
        
        if change < min_delta:
            break
    return authority, hub
    
#================================================
'''
import re
file = open('./Dataset/IBM.txt')
G = digraph()
nodes = []
myline = []

with open('./Dataset/IBM_out.txt', 'w') as f:
    for e in file:
        e= (re.sub(r"[^a-zA-Z0-9,]+", ' ', e))
        f.write("%s\n" % e)
'''
#=================================================        

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

#=================================================        

'''
file = open('./Dataset/graph_1.txt')
G = digraph()

nodes = []
myline = []
for line in file:
    line = line.strip().split(",")
    myline.append(line)
    for node in line:
        nodes.append(node)
#print(myline)
nodes = set(nodes)
#nodes = sorted(nodes, key=lambda x: int(x[0])) 
#print(nodes)
G.add_nodes(nodes)
for i in myline:
    print(i)
    G.add_edge(i)
    #print(i)
#G.add_edge(('1','3'))
#G.add_edge(('4','1'))
#G.del_edge(('3','2'))
'''
#====================================
max_iterations = 1000  
min_delta = 0.00001  

authority = {}
hub = {}

authority, hub = HITS(G,max_iterations,min_delta)
authority = sorted(authority.items(), key=operator.itemgetter(1),reverse=True)
hub = sorted(hub.items(), key=operator.itemgetter(1),reverse=True)

print("Authority:",authority)
print("Hub:",hub)


#=====================================
'''
G = nx.DiGraph()
G.add_edges_from(myline)
#nx.draw(G,with_labels = True, color= 'red', font_weight= 'bold')
'''