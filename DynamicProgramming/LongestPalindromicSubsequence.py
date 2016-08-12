'''
Creation Date: Jul 4, 2016
@author : Santosh Ghosh

Problem Statement: Find the longest palindromic subsequence in a string.

Similar kind of question: Minimum number of chars to be deleted to make a string palindromic

Input: String S

Output: Length of LPS as well as the LPS itself

Logic Applied:
This solution uses recursion. It does not create a DP table like the one mentioned here : https://www.youtube.com/watch?v=_nCsPn7_OgI
So this might be a bit inefficient because of recursive calls. Still the concept is same.

Case-I:
if the s[0] and s[-1] are same then the longest palindromic subsequence should be the lps of
s[1:-1]. Since we have already matched two chars we keep them as part of the lps
Case-II:
when s[0] not equal to s[-1]. So the lps is the the max value of lps amongst
s[0:-1] (excludes rightmost char) and s[1:] (excludes leftmost char)

we also keep track of the lps so far by rerturning it as a tuple along with lps_length
'''

def longestPalindromicSubsequence_Helper(s,tab):
    
    print " "*tab +str(tab)+ "Calling with " + s
    longest_subseq_len = 0
    lps = ""
    if len(s)==2:
        print " "*tab +str(tab)+ "Base case hit with len = 2 "
        if s[0]==s[1]:
            longest_subseq_len = 2
            lps = s
        else:
            longest_subseq_len = 1
            lps = s[0]
    elif len(s)==1:
        print " "*tab +str(tab)+ "Base case hit with len = 1"
        longest_subseq_len = 1
        lps = s
    
    else:
        
        
        if s[0]==s[-1]:
            longest_subseq_len,lps = longestPalindromicSubsequence_Helper(s[1:-1],tab+1)
            longest_subseq_len += 2
            lps = s[0] + lps + s[-1]
        else:
            #case-II 
            
            including_left_char = 0
            including_right_char = 0
            including_left_char,lps_left_char = longestPalindromicSubsequence_Helper(s[0:-1], tab+1)
            including_right_char,lps_right_char = longestPalindromicSubsequence_Helper(s[1:], tab+1)
            (longest_subseq_len,lps) = (including_left_char,lps_left_char) if including_left_char > including_right_char else (including_right_char,lps_right_char)
    print " "*tab +str(tab)+ "Longest palindromic subsequence for " + s + " "+ str(longest_subseq_len) + " LPS: " + lps
    return (longest_subseq_len,lps)

if __name__ == "__main__":
    
    #longestPalindromicSubsequence_Helper("abbaxabbmb", 0)
    longestPalindromicSubsequence_Helper("agbdba", 0)
    
    