class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        set1=set()
        i=1
        while(len(set1)<n):
            
            if k-i not in set1:
                set1.add(i)
            i+=1
        return sum(set1)    
                

                    
                
                    