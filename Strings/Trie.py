class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False

def buildTrie(words):
    root = head  = TrieNode()
    for word in words:
        print "Adding " + word + " to trie"
        head = root
        for ch in word:
            print "Inspecting " + ch
            if ch not in head.children:
                print "Adding character " + ch + " to trie"
                head.children[ch] = TrieNode()
            head = head.children[ch]
        head.endofword = True
    return root


def printAllTrieWords(root):
    printTrieWordsHelper(root, "")

def printTrieWordsHelper(root, strSoFar):
    #print "Traversing " + strSoFar
    if root.endofword and len(root.children.keys()) == 0:
        print strSoFar
        return
    if root.endofword:
        print strSoFar
    for ch in root.children.keys():
        printTrieWordsHelper(root.children[ch], strSoFar + ch)


if __name__ == "__main__":
    words = ["abc", "abgl", "cdf", "abcd", "lmn"]
    trie = buildTrie(words)
    printAllTrieWords(trie)


