## Valid Parentheses

#### **Difficulty level:** Easy

#### **Language Used:** Python

### Runtime: 15 ms 
### Memory: 13.4 MB

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
 

_Example 1:_

Input: s = "()"

Output: true

_Example 2:_

Input: s = "()[]{}"

Output: true

_Example 3:_

Input: s = "(]"

Output: false
 

Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.