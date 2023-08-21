/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var newSet = new Set();
    for (let i = 0; i < nums.length; i += 1) {
        newSet.add(nums[i]);
    }
    let j = 0;
    for (let i of newSet) {
        nums[j] = i;
        j += 1;
    }
    return newSet.size;
};