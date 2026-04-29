import sys

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    k = int(input_data[1])
    limit = int(input_data[2])
    readings = [int(x) for x in input_data[3:3+n]]
    levels = [int(x) for x in input_data[3+n:3+n+k]]
    
    # this solution ingores the nmultipliers altogether
    
    maxlen = 0
    l = 0
    currmin = readings[0]
    currmax = readings[0]
    
    for r in range(n):
        currmin = min(currmin, readings[r])
        currmax = max(currmax, readings[r])
        
        while (currmax - currmin) > limit:
            l += 1
            currmin = min(readings[l:r+1])
            currmax = max(readings[l:r+1])
        
        maxlen = max(maxlen, r - l + 1)
    
    print(maxlen)

if __name__ == '__main__':
    solve()
