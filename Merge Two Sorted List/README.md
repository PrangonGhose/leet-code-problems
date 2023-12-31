## Merge Two Sorted Lists

#### **Difficulty level:** Easy

#### **Language Used:** Python

### Runtime: 29 ms **Beats: 73.55%**
### Memory: 13.4 MB **Beats: 89.76%**

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

_Example 1:_

<img src="merge_ex1.jpg">

Input: `list1 = [1,2,4], list2 = [1,3,4]`

Output: `[1,1,2,3,4,4]`

_Example 2:_

Input: `list1 = [], list2 = []`

Output: `[]`

_Example 3:_

Input: `list1 = [], list2 = [0]`

Output: `[0]`


Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
