class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        s=str(num)
        for i in range(len(s)-k+1):
            if int(s[i:i+k])!=0 and num%int(s[i:i+k])==0:
                count+=1
        return count