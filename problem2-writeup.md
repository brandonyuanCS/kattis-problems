# Problem 2 Writeup

## Problem Goal
The primary goal of this problem is to test the user's ability to identify and implement a trie. The problem requires efficiently answering multiple queries about the frequency of prefixes across some set of strings. For this problem a naive approach, such as checking every query against every message, would result in an O(N * Q * L) time complexity and likely TLE. A trie allows you to compute these prefixes efficiently.

This problem is meant to be a straightforward implementation of a trie which penalizes inefficient string matching. There are also large test cases that ensure the solution has to be memory-efficient.

## Potential Correct Approach
To solve this problem efficiently, the user should construct a Trie where each node stores the character that it represents, and the prefix "count" for that node. You'll notice that because we don't actually care when a word ends, we don't need to store that as a boolean.

For each message (and value) received in the input, you should traverse the trie character by character. For each node visited along the characters in the message, you should add the message's value to that node's count. If a node for a character doesn't exist, you should create it. 

This means that for messages that are brand new, you have to create a new node for each character. For messages with an existing prefix, you increment the existing nodes' counts but create the remaining nodes. For messages that already exist in the trie, you'll just increment the existing nodes.

When querying, you traverse the trie following the characters of the phrase/prefix. If the traversal successfully reaches the end of the phrase, then the resulting node's count is the value you return. If at any point in the traversal you are missing the required node to continue, then it means that the prefix never occurred in the earlier input, and the program should return 0 and continue to the next query.

This approach with a trie takes O(N * L) time to build and O(L) time per query.

## Acknowledgements
I spoke with Susan Hamilton and David Sung on their opinions on this problem, since I ended up choosing a different idea than the one I initially proposed in our meeting.
