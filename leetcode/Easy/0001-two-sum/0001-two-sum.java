class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> vals = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (vals.containsKey(nums[i])) {
                return new int[] {vals.get(nums[i]), i};
            } else {
                vals.put(target - nums[i], i);
            }
        }
        
        return new int[] {0, 0};
    }
}