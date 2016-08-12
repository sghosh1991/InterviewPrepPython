'''
Creation Date: Jul 4, 2016
@author : Santosh Ghosh

Problem Statement: Given a text and a pattern test whether the text matches the pattern. The pattern contains wildcards.
Only two wild cards are there:
1) * <--- 0 or more occurance of a character
2) ? <--- 1 occurance of any character. 

Input: A string called text and a string called pattern.

Output: True <-- if text matches pattern else False

Logic Applied: 

Each element of the aux matrix T represents:
T[i][j] <--- if text[0,i] matches pattern[0,j]. text is in y axis and pattern in x axis
'''


def create_aux_matrix(text,pattern):
    
    T = []
    
    for i in range(len(text)+1):
        T.append([-1]*(len(pattern)+1))
    
    printMatrix(T)
    
    #fill up the first row
    # the first row means match of empty text with pattren. This could be true if and only if all the pattern contained was a *
    #if the pattern contains anything else we fill the rest of the row with False
    # Because this is not regex match this is wildcard matching. So a single non-* char in the pattern means that that char MUST
    #be present in the text as well. But the text is "" for 1st row. So there is no match
    T[0][0]=True
    non_star_char_found = False
    for i in range(1,len(T[0])):
        if not non_star_char_found and pattern[i-1]=="*":
            T[0][i] = True
        else:
            non_star_char_found = True
            T[0][i]=False
    printMatrix(T)
    
    #fill up the first column
    #This means we are trying to match the empty pattern with the text. Any kind of text apart from empty text will NOT
    #match the empty pattern. So we fill this col with false except the 1st row 1st col which represents match pf the
    #empty text and empty pattern
    for i in range(1,len(T)):
        #print i
        T[i][0] = False
    
    printMatrix(T)
    
    #fill up the remaining cells
    for row in range(1,len(T)):
        for col in range(1,len(T[0])):
            
            if pattern[col-1]==text[row-1] or pattern[col-1]=="?":
                T[row][col] = T[row-1][col-1]
            elif pattern[col-1]=="*":
                T[row][col] = T[row-1][col] or T[row][col-1]
            else:
                T[row][col] = False
    
    printMatrix(T)
    return T

    
def printMatrix(T):
    for row in range(len(T)):
        print T[row]
    print "\n"


if __name__ == "__main__":
    text = "xaylmz"
    pattern = "?*"
    
    print "Does " + text + " match " + pattern + " ? " + str(create_aux_matrix(text, pattern)[len(text)][len(pattern)]) 
