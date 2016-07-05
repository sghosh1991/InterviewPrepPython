'''
Creation Date: Jun 28, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied:
'''

class Stack():
    
    def print_stack(self):
        print self.__stack
        print self.__aux
        print "="*10
    
    def __init__(self):
        
        self.__aux = [] #auxiliary stack to keep track of max till now
        self.__stack = [] #list to hold the stack data
    
    
    def push(self,elem):
        
        if len(self.__aux)==0:
            self.__aux.append([elem,1])     
        else:
            if self.__aux[-1][0] < elem:
                self.__aux.append([elem,1])
            elif self.__aux[-1][0] == elem:
                self.__aux[-1][1] +=1
        
        self.__stack.append(elem)
    
    
    def pop(self):
        
        if self.__stack[-1] == self.__aux[-1][0]:
            self.__aux[-1][1] -= 1
            if  self.__aux[-1][1]==0:
                self.__aux = self.__aux[:-1]
        
        popped_elem = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return popped_elem
    
    def max(self):
        return self.__aux[-1][0]
            
    
if __name__ == '__main__':
    
    s = Stack()
    s.push(2)
    s.print_stack()
    s.push(2)
    s.print_stack()
    s.push(1)
    s.print_stack()
    s.push(4)
    s.print_stack()
    s.push(5)
    s.print_stack()
    s.push(5)
    s.print_stack()
    s.push(3)
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
    s.push(0)
    s.print_stack()
    s.push(3)
    s.print_stack()
    
                                