class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = 0

        arr.sort()

        for i in range(len(arr)):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == target:
                    if arr[left] == arr[right]:
                        n = right - left + 1
                        count += n * (n - 1) // 2
                        break
                    else:
                        l = 1
                        r = 1

                        while left + l < right and arr[left + l] == arr[left]:
                            l += 1

                        while right - r > left and arr[right - r] == arr[right]:
                            r += 1

                        count += l * r
                        left += l
                        right -= r

                elif total < target:
                    left += 1
                else:
                    right -= 1

        return count % MOD