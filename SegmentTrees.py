

class Node():
    
    value=""
    interval=""
    left=""
    right=""
    
    def __init__(self,interval,value,left,right):
        
        self.interval = interval
        self.left = left
        self.right = right
        self.value = value
        


class SegmentTree():
    
    root = ""
    
    
    def __init__(self,arr,lo,hi):
        
        self.root = self.insert(arr, lo, hi)  

    def totalOverlap(self,range1,range2):
        
        #does range1 totally overlap range2
        
        if(range1[0]<= range2[0] and range1[1]>=range2[1]):
            return True
    
    
    def noOverlap(self,range1,range2):
        
        if(range1[0] > range2[1] or range1[1] < range2[0] ):
            
            return True
    
    
    
    def insert(self,arr,lo,hi):
        
        #print ("prosessing " + str((lo,hi)))
        
        if(abs(lo-hi)==1):
            
            leftChild = Node((lo,lo),arr[lo],None,None)
            rightChild = Node((hi,hi),arr[hi],None,None)
            
            parent = Node((lo,hi),"",leftChild,rightChild)
            parent.value = min(leftChild.value,rightChild.value)
            return parent
            
        if(lo==hi):
            
            return Node((lo,lo),arr[lo],None,None)
        
        
        mid = (lo+hi)/2
        
        n = Node((lo,hi), "",None,None)
        n.left = self.insert(arr,lo,mid)
        n.right = self.insert(arr,mid+1,hi)
        
        n.value = min(n.left.value,n.right.value)
        
        return n
    
    def rangeMin(self,lo,hi,root):
        
        if(self.totalOverlap((lo,hi),root.interval)):
           
           return root.value
       
        if (self.noOverlap((lo,hi), root.interval)):
            
            return 99999
        
        else:
            
            return min(self.rangeMin(lo, hi, root.left) , self.rangeMin(lo, hi, root.right))
    
    
    def inooder(self,x):
        
        if(x==None):
            return
        
        self.inooder(x.left)
        print(x.value)
        self.inooder(x.right)
        
    

if __name__ == "__main__":
    
    arr = [-1,3,4,0,2,1]
    
    s = SegmentTree(arr,0,len(arr)-1)
    
    #s.inooder(s.root)
    
    print (s.rangeMin(4, 5, s.root))
    
    
    
       


    
    
        
    