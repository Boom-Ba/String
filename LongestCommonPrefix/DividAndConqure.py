class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def findCommonPrefix(s1,s2):
            if not s1 or not s2:
                return ''
            retStr= ''
            i,j =0,0
            while i<len(s1) and j<len(s2):
                if s1[i]==s2[j]:
                    retStr=s1[:i+1]
                    i+=1
                    j+=1
                else:
                    break
            return retStr
        
        def divid(a, left,right):
            if not a:
                return 
            if left>right:
                return 
            if left==right:
                return a[left]
            
            mid=left+(right-left)//2
            prefix1= divid(a, left,mid)
            prefix2= divid(a, mid+1,right)
            res =findCommonPrefix(prefix1,prefix2)
            return res
        
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]
        return divid(strs, 0,len(strs)-1)
        
    
