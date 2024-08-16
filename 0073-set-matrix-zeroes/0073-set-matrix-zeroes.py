
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        rowarr = [0]*n
        colarr = [0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    rowarr[i] = 1 
                    colarr[j] = 1
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]!=0:
                    if rowarr[i] == 1 or colarr[j]== 1 :
                        matrix[i][j] = 0 
        
        return matrix


        
        

        

        
        
