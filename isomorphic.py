

def isIsomorphic(str1,str2):
    
    if(len(str1) != len(str2)):
        return False
    
    map1 = dict()
    map2 = dict()
    
    for c1,c2 in zip(str1,str2):
        
        map1[c1] = map1.get(c1,0) + 1
        map2[c2] = map2.get(c2,0) + 1
    print "map1"
    print map1
    
    #print map2
    
    reverseMap2 = dict()
    
    for key,value in map2.items():
        
        #print key,value
        x = reverseMap2.get(value,[])
        #print x 
        x.append(key)     
        reverseMap2[value] = x
        #print reverseMap2
    
    print "reversemap"
    print reverseMap2
    
    
    
    for key in map1.keys():
        
        print map1[key]
        #print reverseMap2[map1[key]]
        #x = reverseMap2.keys()
        
        
        if(map1[key] in reverseMap2):
            
            print "here1"
           
            reverseMap2[map1[key]] = reverseMap2[map1[key]][1:]
            print "here2"
            if(len(reverseMap2[map1[key]]) == 0):
                reverseMap2.pop(map1[key])
            
            print "here3"
            print reverseMap2
            
            
        else:
            print "Cant find " + str(map1[key])
            return False 
                
        
    
    return True

if __name__ == "__main__":
    
    if(isIsomorphic("AOOT", "EDRE")):
        print "True"
    else:
        print "False"