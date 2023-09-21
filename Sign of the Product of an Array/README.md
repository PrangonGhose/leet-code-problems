## Sign of the Product of an Array

#### **Difficulty level:** Easy

#### **Language Used:** Python

### Runtime: 12 ms **Beats: 81.94%**

### Memory usage: 14 MB **Beats: 64%**

There is a function signFunc(x) that returns:

- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return `signFunc(product)`.

_Example 1:_

Input: nums = [-1,-2,-3,-4,3,2,1]

Output: 1

Explanation: The product of all values in the array is 144, and `signFunc(144) = 1`

_Example 2:_

Input: nums = [1,5,0,2,-3]

Output: 0

Explanation: The product of all values in the array is 0, and `signFunc(0) = 0`

_Example 3:_

Input: nums = [-1,1,-1,1,-1]

Output: -1

Explanation: The product of all values in the array is -1, and `signFunc(-1) = -1`

**Constraints:**

- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100
