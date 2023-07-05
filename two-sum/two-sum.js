/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    vals = {}
    for(var i=0;i<nums.length;i++){
        if(nums[i] in vals){
            return [vals[nums[i]], i]
        }else{
            vals[target-nums[i]]=i
        }
    }
};