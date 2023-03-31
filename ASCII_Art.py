import sys
import math
from string import ascii_lowercase

l = int(input())
h = int(input())
t = input()


arr = []
for i in range(h):
    row = input()
    arr.append([row[x:x+l] for x in range(0, len(row), l)])
    print(arr[i], file=sys.stderr, flush=True)

idx = [ord(char) - 97 for char in t.lower()]

for u in range(h):
    string = ""
    for num in idx:
        try:
            string += arr[u][num]
        except:
            string += arr[u][-1]
    print(string)