class Solution(object):
    def distinctIntegers(self, n):
        x=[n]
        for i in range(1,n):
            for i in range(1,n):
                if n%i==1:
                    x.append(i)
                n=i
        return len(x)
      