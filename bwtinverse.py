# python3
import sys


def InverseBWT3(bwt):
    last = [(val, idx)  for (idx, val) in enumerate(bwt)]
    first = sorted(last)
    first_to_last = {f: l for f, l in zip(first, last)}
    
    next_ele = first[0]
    result = ''
    for i in range(len(bwt)):
        result += next_ele[0]
        next_ele = first_to_last[next_ele]

    return result[::-1]


def InverseBWT(bwt):
    # write your code here
    
    last = list(bwt)
    n = len(bwt)
    first = last[:]
    first.sort()
    ele = first[0]
    temp = []
    num = 1

    for i in range(n):
        #从f[0] $第一个元素开始，它的坐标在l中的元素，是下一个字符，确定它在l中排第几
        #然后再把这个字符找到对应的f里面的位置，循环往复n次。
        value = 0
        for j in range(n):
            if ele==first[j]:
                value = value+1
            if value == num:
                rank = j
                break
        temp.insert(0,ele)
        next_ele = last[rank]

        num = last[:rank].count(next_ele)+1
        ele = next_ele
        first.pop(rank)
        last.pop(rank)
    temp = ''.join(temp)
    return temp

def InverseBWT2(bwt):
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
    #bwt = 'TTCCTAACG$A'
    print(InverseBWT3(bwt))
