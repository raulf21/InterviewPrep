"""For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""


def gcdOfStrings(str1, str2):
    def gcd(a,b):
        while b:
            a,b = b, a % b
        return a
    
    len1, len2 = len(str1), len(str2)
    gcd_len = gcd(len1,len2)

    substring = str1[:gcd_len]

    return substring * (str1 == substring * (len1// gcd_len)) * (str2 == substring * (len2 // gcd_len))

 