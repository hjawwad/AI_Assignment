# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:16:28 2020

@author: Hp
"""
import numpy as np
from collections import deque 


    

class Node:

    def __init__(self,state,parent,action):

        self.state = state;
        self.action = action;
        self.cost = 0;
        self.parent = parent;
        self.child = None;
    


    
    
def BREADTH_FIRST_SEARCH(problem,noOfActions):
    node = Node(problem[0],None,"")
    frontier = deque()
    explored = deque()
    frontier.append(node)
    while(True):
        if(not frontier):
            return None
        node = frontier.pop()
        if(goal_Test(node,problem[1])):
            return node
        explored.append(node.state)
        for x in range(noOfActions):
            child = Node(states.get(transitionTable[states.indexOf(node.state)][i]), node, actions.get(i))
            if(not is_Member_frontier(frontier,child) and not member_of_explored(explored, child.state)):
                if( goal_Test(child,problem[1])):
                    return child
                else:
                    frontier.append(child)
                    
            

def goal_Test(node,goal):
    return (node.state == goal)

def member_of_explored(ex,state):
    for x in range(ex):
        if x == state:
            return True
    
    return False
    
def is_Member_frontier(fr,node):
    for x in range(fr):
        if x == state:
            return True
        
    return False
    
    
    
    
print("Welcome to goal based agent")
input_file = open("file.txt", "r")
transition_matrix = []
frontier = deque()
########input_file reading########
stat = input_file.readline();
print(input_file.readline())
stat = stat.split()
states = int(stat[0])
rule = int(stat[1])
cases = int(stat[2])

description = []
for x in range(2,states+2):
    description.append(input_file.readline())
input_file.readline()
rule_discription = []
for x in range(states+3, states+rule+3):
    rule_discription.append(input_file.readline())


input_file.readline()
for i in range(0,states):
    line = input_file.readline().split()
    for j in range(0,rule):
        transition_matrix.append(int(line[j]))

transition_matrix = np.array(transition_matrix) 
    
transition_matrix.resize(states,rule)
print(transition_matrix)
ini_fin_state = input_file.readline()
i=0
while(i<2):
    print(ini_fin_state)
    ini_fin_state = input_file.readline()
    i+=1
    #Plan plan = new Plan()
    #BREADTH_FIRST_SEARCH(ini_fin_state)
    #ini_fin_state = input_file.readline()
    
########input_file reading done##########
    



