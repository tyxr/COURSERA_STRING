# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  P = pattern + '$' + text
  Len = len(list(P))
  result = []
  border = 0
  s = [0 for _ in range(Len)]
  for i in range(1,Len):
    while border>0 and P[i]!=P[border]:
      border = s[border-1]
    if P[i]==P[border]:
      border = border+1
    else:
      border = 0
    s[i]=border
  lenpatten= len(list(pattern))
  num = 2*lenpatten
  for i in range(lenpatten+1,Len):
    if s[i]==lenpatten:
      result.append(i-num)
  # Implement this function yourself
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  #pattern = 'ATA'
  #text = 'ATATA'
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

