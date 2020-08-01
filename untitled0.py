# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:56:26 2020

@author: chris
"""
class Node:
    def __init__(self , value = None):
        self.value = value
        self.left = None
        self.right = None
node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node("apple")
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")
    