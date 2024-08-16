def bin_search(arr,target) : 
    n = len(arr)
    low , high = 0 , n-1
    while low <= high : 
        mid = (low+high)//2
        if arr[mid]==target :
            return True
        elif target < arr[mid] : 
            high = mid-1
        else : 
            low = mid+1
    return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]: 
                return bin_search(matrix[i],target)
        return False
                