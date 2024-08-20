class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # D = defaultdict(int)
        # for i in s : 
        #     D[i]+=1 
        # for i in t :
        #     if i not in D.keys() :
        #         return False 
        #     else : 
        #         D[i]-=1
        # for i,j in D.items(): 
        #     if j!=0 :
        #         return False
        # return True
        
        return all(s.count(x)==t.count(x) for x in set(s+t))