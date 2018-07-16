class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False

def buildTrie(words):
    root = head  = TrieNode()
    for word in words:
        #print "Adding " + word + " to trie"
        head = root
        for ch in word:
            #print "Inspecting " + ch
            if ch not in head.children:
                #print "Adding character " + ch + " to trie"
                head.children[ch] = TrieNode()
            head = head.children[ch]
        head.endofword = True
    return root


def lookup(s, trie):
    return lookupHelper(s, 0, trie)

def lookupHelper(s, pos, trie):

    if pos == len(s):
        return trie.endofword
    if s[pos] not in trie.children:
        return False

    return lookupHelper(s, pos + 1, trie.children[s[pos]])


def prefixToUniquelyIdentifyString(s, trie)
    pass

def prefixToUniquelyIdentifyStringHelper(s, trie):


def printAllTrieWords(root):
    printTrieWordsHelper(root, "")

def printTrieWordsHelper(root, strSoFar):
    if root.endofword:
        print strSoFar
        return
    for ch in root.children.keys():
        printTrieWordsHelper(root.children[ch], strSoFar + ch)


if __name__ == "__main__":
    words = ["abc", "abgl", "cdf", "abcd", "lmn"]
    trie = buildTrie(words)
    printAllTrieWords(trie)
    print lookup("abg", trie)


