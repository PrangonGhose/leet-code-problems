## Two Sums

#### **Difficulty level:** Easy

#### **Language Used:** Python

### Runtime: 542 ms **Beats: 51.28%**
### Memory: 14.3 MB **Beats: 32.54%**

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

_Example 1:_

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

_Example 2:_

Input: nums = [3,2,4], target = 6

Output: [1,2]

_Example 3:_

Input: nums = [3,3], target = 6

Output: [0,1]
 

Constraints:

2 <= nums.length <= 104

-109 <= nums[i] <= 109

-109 <= target <= 109

Only one valid answer exists.
 

**Follow-up:** Can you come up with an algorithm that is less than O(n2) time complexity?