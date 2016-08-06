'''
Creation Date: 2016-08-05

@author : Santosh Ghosh

Problem Statement:

Input: The root a a tree

Output: A string representation of the tree.

Logic Applied:

'''

width_mapping = {}
max_left = -2

import collections

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
    
def getChildren(nodes):
    
    children = []
    for node in nodes:
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            #print "adding " + node.right.val
            children.append(node.right)
    return children
        

def createWidthMappings(root):
    
    createWidthMappingsHelper(root,0)

def createWidthMappingsHelper(root,width):
    
    global width_mapping
    if root is None:
        return
    createWidthMappingsHelper(root.left,width-1)
    width_mapping[root] = width
    createWidthMappingsHelper(root.right,width+1)


def drawTree(root):
    
    global width_mapping,max_left
    q1 = []
    q2 = []
    
    q1.append(root)
    
    while True:
        
        to_print=""
        prev_offset_from_left = 0
        while len(q1)!=0:
            
            if len(q1)>1 and width_mapping[q1[0]] == width_mapping[q1[1]]:
                node_to_process = [q1[0],q1[1]]
                offset_from_left =  width_mapping[q1[0]] - max_left - prev_offset_from_left
                prev_offset_from_left = offset_from_left
                to_print += "\t"*offset_from_left + q1[0].val + q1[1].val
                q1=q1[2:]
                children = getChildren(node_to_process)
            else:
                node_to_process = q1[0]

                offset_from_left =  width_mapping[node_to_process] - max_left - prev_offset_from_left
                prev_offset_from_left = offset_from_left
                to_print += "\t"*offset_from_left + node_to_process.val
                q1=q1[1:] #deque the element
                children = getChildren([node_to_process])
                
                
            for child in children:
                q2.append(child)
            
        print to_print + "\n\n"
        if  len(q2)!=0:
            #children were added
            q1,q2=q2,q1
        else:
            break


if __name__ == "__main__":
    
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    
    a.left=b
    a.right=c
    b.right=d
    b.left=f
    c.left=e
    c.right=g
 
    createWidthMappings(a)
    #print width_mapping
    
    drawTree(a)
    
    #print width_mapping[a]
        
            
        
    
