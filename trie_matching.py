# python3
import sys
# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def build_trie(patterns):
        tree = dict()
        tree[0] = {}
        index = 1
        for pattern in patterns:
                current = 0
                for i in list(pattern):
                        if i in tree[current].keys():
                                current = tree[current][i]
                        else:
                                tree[index] = {}
                                tree[current][i] = index
                                current = index
                                index = index+1
                        
        return tree

def match(text,i,tree):
        node = 0
        b = i
        while text[i] in tree[node].keys():
                node = tree[node][text[i]]# node is a number
                i=i+1

                if tree[node] =={}:
                        
                        return b
                if i>=len(text):
                        break

def solve (text, n, patterns):
        tree = build_trie(patterns)
        result = []
        text = list(text)
        for i in range(len(text)):
                if match(text,i,tree) or match(text,i,tree)==0:
                        result.append(match(text,i,tree))            
		
        
        return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
        patterns += [sys.stdin.readline ().strip ()]

'''
text = 'A'
patterns = ['A']
n = 1
'''
ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
