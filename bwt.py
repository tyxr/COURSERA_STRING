# python3
import sys

def BWT(text):
    matrix = []
    text = list(text)
    
    for i in range(len(text)):
        text = list(text[-1])+text[:-1]
        matrix.append(text)
    matrix.sort()
    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i][-1])
    #matrix = sorted(matrix, key=lambda row: ord(row[0]))
    temp = ''.join(temp)
    return temp

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = "ACACACAC$"
    print(BWT(text))
