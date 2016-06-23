'''
Creation Date: 2016-06-23

@author : Santosh Ghosh, Engineer, Quantil Inc.

Problem Statement: Find the minimum number of characters needed to be removed to make a string palindrome

Input: String s

Output: Minimum number of characters to be deleted.

Logic Applied:

'''

def minCharactersToDelete(s,tab):
    
    print "\t"*tab + "Called with :  " + s
    
    if len(s) == 1:
        
        return 0
    
    # Contains the number of deleteions needed if we delete the first character and then proceed.
    delete_first_char = 0
    # Contains the number of deleteions needed if we delete the last character and then proceed.
    delete_last_char = 0
    
    x = 0
    
    if s[0] == s[-1]:
        #print "\t"*tab + "Returning from call to :  " + s
        x =  minCharactersToDelete(s[1:-1],tab+1)   
    else:
        delete_first_char = minCharactersToDelete(s[1:],tab+1)
        delete_last_char = minCharactersToDelete(s[0:-1],tab+1)
        
        
        x =  min([delete_first_char,delete_last_char]) + 1
    print "\t"*tab + "Returning " + str(x)
    return x
    
    
    

if __name__ == "__main__":
    print minCharactersToDelete("anuj", 0)
    
    