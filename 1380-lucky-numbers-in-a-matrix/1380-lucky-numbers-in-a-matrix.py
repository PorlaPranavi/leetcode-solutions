class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        for row in matrix:
            l.append(min(row))
        rows=len(matrix)
        c=len(matrix[0])
        r=[]
        for j in range(0,c):
            o=[]
            for i in range(0,rows):
                o.append(matrix[i][j])
            if max(o) in l:
                r.append(max(o))
        return r
        