class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lookup ={}

        res =0
        for w in sorted(words, key=lambda x: len(x)):
            maxL =1
            for i in range(len(w)):
                temp= w[:i]+w[i+1:]
                if temp in lookup:
                    maxL = max(maxL, lookup[temp] + 1)
            lookup[w] = maxL
            res = max(res, lookup[w])
        return res
                
                
                
