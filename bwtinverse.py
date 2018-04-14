# python3
import sys

def InverseBWT(bwt):
    # write your code here
    
    bwt = list(bwt)
    n = len(bwt)
    matrix = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            matrix[j].insert(0,bwt[j])
        matrix.sort()
    temp = matrix[0][1:]+list(matrix[0][0])
    temp = ''.join(temp)
    return temp


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #bwt = 'AC$A'
    print(InverseBWT(bwt))
