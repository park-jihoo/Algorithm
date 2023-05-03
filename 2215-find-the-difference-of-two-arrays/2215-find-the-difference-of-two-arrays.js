/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    let dif1 = new Set(nums1.filter(x => !nums2.includes(x)))
    let dif2 = new Set(nums2.filter(x => !nums1.includes(x)))
    let answer = [Array.from(dif1), Array.from(dif2)];
    return answer;
};
