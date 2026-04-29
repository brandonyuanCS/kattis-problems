import sys
import re

def verify():
    data = sys.stdin.read()

    # Reject if file doesn't end with exactly one newline
    if not data.endswith('\n') or data.endswith('\n\n'):
        sys.exit("Error: Input must end with exactly one newline")

    # Split into lines (remove trailing newline first)
    lines = data.rstrip('\n').split('\n')

    # Must be exactly 4 lines
    if len(lines) != 4:
        sys.exit(f"Error: Expected exactly 4 lines, found {len(lines)}")

    # Reject trailing/leading spaces on any line
    for i, line in enumerate(lines):
        if line != line.strip():
            sys.exit(f"Error: Line {i+1} has leading/trailing whitespace")
        if '  ' in line:
            sys.exit(f"Error: Line {i+1} has consecutive spaces")

    # Reject leading zeros on any integer token
    for i, line in enumerate(lines):
        for token in line.split():
            if re.match(r'^0\d', token):
                sys.exit(f"Error: Line {i+1} has integer with leading zero: {token}")

    # Line 1: n and k
    l1 = lines[0].split()
    if len(l1) != 2:
        sys.exit(f"Error: Line 1 must have exactly 2 integers. Found {len(l1)}.")
    n, k = int(l1[0]), int(l1[1])

    assert 1 <= n <= 10**5, f"n={n} is out of bounds (1 to 10^5)"
    assert 1 <= k <= 10**5, f"k={k} is out of bounds (1 to 10^5)"

    # Line 2: limit
    l2 = lines[1].split()
    if len(l2) != 1:
        sys.exit(f"Error: Line 2 must have exactly 1 integer. Found {len(l2)}.")
    limit = int(l2[0])
    assert 1 <= limit <= 10**9, f"limit={limit} is out of bounds (1 to 10^9)"

    # Line 3: stress readings array
    l3 = lines[2].split()
    if len(l3) != n:
        sys.exit(f"Error: Line 3 must have exactly {n} integers. Found {len(l3)}.")
    for x in l3:
        val = int(x)
        assert 1 <= val <= 10**9, f"Stress reading {val} is out of bounds (1 to 10^9)"

    # Line 4: levels array
    l4 = lines[3].split()
    if len(l4) != k:
        sys.exit(f"Error: Line 4 must have exactly {k} integers. Found {len(l4)}.")

    prev_level = 0
    for x in l4:
        val = int(x)
        assert 1 <= val <= n, f"Level {val} is out of bounds (must be <= n)"
        assert val > prev_level, f"Levels must be strictly increasing. {val} is not > {prev_level}"
        prev_level = val

    sys.exit(42)

if __name__ == '__main__':
    try:
        verify()
    except AssertionError as e:
        sys.exit(str(e))
    except ValueError as e:
        sys.exit(f"Value error (non-integer found): {e}")