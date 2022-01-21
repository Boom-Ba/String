"""
apple
[a] [pple]
[ap] [ple]
[app] [le]
[appl][e]
Trie:  apple#apple 

n is len(words), m is maximum len of word, k is cost of f, and the maximum length search word is m 
time :( n*m^2 + m*k  )
"""
class Node:
    def __init__(self):
        self.children={}
        self.maxindex=0

class WordFilter:
  
    def __init__(self, words: List[str]):
        self.root=Node()
        for idx,word in enumerate(words):
            
            word= word +'#'+ word
            for i in range(len(word)):
                curr= self.root
                for j in range(i,len(word)):
                    if word[j] not in curr.children:
                        curr.children[word[j]]=Node()
                    curr=curr.children[word[j]]
                    curr.maxindex=idx
    
    """
    Search the index of world if its prefix and suffix both in the words, and return the largest index
    """
    def f(self, prefix: str, suffix: str) -> int:
        #app[le] #[app]le
        curr=self.root
        for k,v in curr.children.items():
            print(k,v)
        sufpre= suffix+'#'+ prefix
        for char in sufpre:
            if char not in curr.children:
                print(char)
                return -1
            curr=curr.children[char]
        return curr.maxindex
        
