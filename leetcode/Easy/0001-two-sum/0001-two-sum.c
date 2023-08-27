/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* result = (int*)malloc(2 * sizeof(int));
        int vals[numsSize];

        for (int i = 0; i < numsSize; i++) {
            if (i > 0) {
                for (int j = 0; j < i; j++) {
                    if (vals[j] == nums[i]) {
                        result[0] = j;
                        result[1] = i;
                        *returnSize = 2;
                        return result;
                    }
                }
            }
            vals[i] = target - nums[i];
        }

        *returnSize = 0;
        return result;
}