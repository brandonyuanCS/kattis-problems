import sys

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    k = int(input_data[1])
    limit = int(input_data[2])
    readings = [int(x) for x in input_data[3:3+n]]
    levels = [int(x) for x in input_data[3+n:3+n+k]]
    
    # Precompute multipliers for each possible window length
    multipliers = [1] * (n + 1)
    i = 0
    currmult = 1
    for length in range(1, n + 1):
        while i < k and length > levels[i]:
            currmult += 1
            i += 1
        multipliers[length] = currmult

    maxlen = 0
    l = 0
    for r in range(n):
        while l <= r:
            # TLE bottleneck: recompute min and max by scanning the entire window
            window = readings[l:r+1]
            currmin = min(window)
            currmax = max(window)
            
            len_currwindow = r - l + 1
            mult = multipliers[len_currwindow]
            
            if (currmax - currmin) * mult <= limit:
                break
            else:
                l += 1
                
        maxlen = max(maxlen, r - l + 1)
    print(maxlen)

if __name__ == '__main__':
    solve()
