class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #for i in range(len(arr)-1):
            #arr[i] = max(arr[i+1:])
        #arr[-1] = -1
        #return arr
        max = -1
        for i in range(1, len(arr)+1):
            prev_max = max
            if arr[-i] > max:
                max = arr[-i]
            arr[-i] = prev_max
        return arr

