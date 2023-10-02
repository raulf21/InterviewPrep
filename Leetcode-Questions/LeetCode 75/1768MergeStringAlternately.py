''' 
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

'''

def mergeAlterhanetly(word1:str, word2:str):
    s = ''
    # Compare the lengths of word1 and word2
    if len(word1) < len(word2):
        for i in range(len(word1)):
            s += word1[i] + word2[i]  # Merge characters alternately
        s += word2[i+1:]  # Append the remaining characters of word2
    elif len(word1) > len(word2):
        for i in range(len(word2)):
            s += word1[i] + word2[i]  # Merge characters alternately
        s += word1[i+1:]  # Append the remaining characters of word1
    else:
        for i in range(len(word1)):
            s += word1[i] + word2[i]  # Merge characters alternately
    return s


"""Overall, the time complexity can be expressed as:

If n == m: O(n)
If n != m: O(min(n, m) + abs(n - m))

Overall, the space complexity can be expressed as:

O(n + m)
"""