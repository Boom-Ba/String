class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res=[]
        
        s=''
        for idx, w in enumerate(searchWord):
            s+=w
            temp=[]
            for product in products:
                if product[:idx+1]==s:
                    temp.append(product)
            
            temp.sort()
            if len(temp)>3:
                temp =temp[:3]
            
            res.append(temp)
        return res
                    
            
