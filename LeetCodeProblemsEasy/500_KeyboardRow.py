'''

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alphabets_by_row = {
            'a':2,
            'b':3,
            'c':3,
            'd':2,
            'e':1,
            'f':2,
            'g':2,
            'h':2,
            'i':1,
            'j':2,
            'k':2,
            'l':2,
            'm':3,
            'n':3,
            'o':1,
            'p':1,
            'q':1,
            'r':1,
            's':2,
            't':1,
            'u':1,
            'v':3,
            'w':1,
            'x':3,
            'y':1,
            'z':3,
            'A':2,
            'B':3,
            'C':3,
            'D':2,
            'E':1,
            'F':2,
            'G':2,
            'H':2,
            'I':1,
            'J':2,
            'K':2,
            'L':2,
            'M':3,
            'N':3,
            'O':1,
            'P':1,
            'Q':1,
            'R':1,
            'S':2,
            'T':1,
            'U':1,
            'V':3,
            'W':1,
            'X':3,
            'Y':1,
            'Z':3
        }
        res = []
        for word in words:
            row = alphabets_by_row[word[0]]
            res.append(word)
            #print word
            for ch in word[1:]:
                #print ch + ":" + str(row) + ":" + str(alphabets_by_row[ch])
                if alphabets_by_row[ch] != row:
                    res = res[:-1]
                    break
                row = alphabets_by_row[ch]
        return res