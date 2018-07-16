"""
https://leetcode.com/problems/alien-dictionary/description/

There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this
 new language. Derive the order of letters in this language.


Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Hidde topo sort. Create the dependency or ordering graph from words.
Then run topo sort

"""

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.char_ordering = {}
        for word in words:
            for ch in word:
                self.char_ordering[ch] = set()

        for i in range(1, len(words)):
            for ch1, ch2 in zip(words[i-1], words[i]):
                if ch1 != ch2:
                    self.char_ordering[ch1].add(ch2)
                    break

        print self.char_ordering
        self.discovered = set()
        self.processed = set()
        self.dictionary = []
        self.cycle = 0
        for ch in self.char_ordering.keys():
            if ch not in self.discovered:
                self.dfs(ch)
        if self.cycle:
            self.dictionary = []
        return "".join(self.dictionary[::-1])


    def dfs(self, node):

        self.discovered.add(node)
        for neighbor in self.char_ordering[node]:
            if neighbor in self.processed:
                continue
            if neighbor in self.discovered:
                self.cycle = 1
                return
            else:
                self.dfs(neighbor)
        self.processed.add(node)
        self.dictionary.append(node)



if __name__ == "__main__":
    x = Solution()
    words = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    print ">>" + x.alienOrder(words) + "<<"

    words = ["z", "x"]
    print ">>" + x.alienOrder(words) + "<<"

    words = ["z", "x", "z"]
    print ">>" + x.alienOrder(words) + "<<"

    words = ["za","zb","ca","cb"]
    print ">>" + x.alienOrder(words) + "<<"
