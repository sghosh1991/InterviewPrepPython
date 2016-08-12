'''
Creation Date: Jul 4, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied:
'''

def longestPalindromicSubstring_Helper(s,tab):
    
    print " "*tab +str(tab)+ "Calling with " + s
    longest_substr_len = 0
    lps = ""
    if len(s)==2:
        print " "*tab +str(tab)+ "Base case hit with len = 2 "
        if s[0]==s[1]:
            longest_substr_len = 2
            lps = s
        else:
            longest_substr_len = 1
            lps = s[0]
    elif len(s)==1:
        print " "*tab +str(tab)+ "Base case hit with len = 1"
        longest_substr_len = 1
        lps = s
    
    else:
        
        
        if s[0]==s[-1]:
            longest_substr_len,lps = longestPalindromicSubstring_Helper(s[1:-1],tab+1)
            longest_substr_len += 2
            lps = s[0] + lps + s[-1]
        else:
            #case-II 
            
            including_left_char = 0
            including_right_char = 0
            including_left_char,lps_left_char = longestPalindromicSubstring_Helper(s[0:-1], tab+1)
            including_right_char,lps_right_char = longestPalindromicSubsequence_Helper(s[1:], tab+1)
            (longest_substr_len,lps) = (including_left_char,lps_left_char) if including_left_char > including_right_char else (including_right_char,lps_right_char)
    print " "*tab +str(tab)+ "Longest palindromic subsequence for " + s + " "+ str(longest_substr_len) + " LPS: " + lps
    return (longest_substr_len,lps)

if __name__ == "__main__":
    
    longestPalindromicSubsequence_Helper("abbaxabbmb", 0)