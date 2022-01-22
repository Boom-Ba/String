class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
 
        # if size is 0, return empty string
        if (size == 0):
            return ""

        if (size == 1):
            return strs[0]
 
        # sort the array of strings
        strs.sort()
     
        print(strs)
        # find the minimum length from
        # first and last string
        end = min(len(strs[0]), len(strs[size - 1]))
        #find common prefix from first string and last
        i = 0
        while (i < end and strs[0][i] == strs[size - 1][i]):
            i += 1
 
        pre = strs[0][0: i]
        return pre
