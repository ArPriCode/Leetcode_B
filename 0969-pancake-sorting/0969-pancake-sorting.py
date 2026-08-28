class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        def dfs(arr,max_val):
            nonlocal ans
            if max_val==0:
                return True
            for i in range(max_val):
                if arr[i]==max_val:
                    idx=i 
                    break
            if idx+1!=max_val:
                arr=((arr[:idx+1][::-1]+arr[idx+1:])[::-1])[:-1]
                ans.append(idx+1)
                ans.append(max_val)
                if dfs(arr,max_val-1):
                    return True
            else:
                if dfs(arr[:idx],max_val-1):
                    return True
            return False
        dfs(arr,len(arr))
        return ans