# python3
import sys
def BWT(text):
    matrix = []
    text = list(text)
    n = len(text)
    num = list(range(n-1,0,-1))
    num.insert(0, 0)

    for i in range(n):
        temp =text[:n-num[i]]
        matrix.append([num[i],temp])
        text = list(text[-1])+text[:-1]
    
    matrix.sort(key=lambda x:x[1])
    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i][0])
    #matrix = sorted(matrix, key=lambda row: ord(row[0]))
    
    return temp


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  
  result = []
  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, BWT(text))))
