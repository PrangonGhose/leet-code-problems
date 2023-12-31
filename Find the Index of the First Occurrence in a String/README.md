## Find the Index of the First Occurrence in a String

#### **Difficulty level:** Easy

#### **Language Used:** Python

### Runtime: 13 ms **Beats: 98%**
### Memory: 13.5 MB **Beats: 34%**

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

_Example 1:_

**Input:** `haystack = "sadbutsad", needle = "sad"`

**Output:** `0`

**Explanation:** `"sad"` occurs at index 0 and 6.

The first occurrence is at index 0, so we return 0.

Example 2:

**Input:** `haystack = "leetcode", needle = "leeto"`

**Output:** `-1`

**Explanation:** `"leeto"` did not occur in "leetcode", so we return -1.
 

**Constraints:**

- `1 <= haystack.length, needle.length <= 104`
- `haystack` and `needle` consist of only lowercase English characters.
