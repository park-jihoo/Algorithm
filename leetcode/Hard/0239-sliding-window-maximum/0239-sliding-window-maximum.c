/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    int* res = (int*)malloc((numsSize - k + 1) * sizeof(int));
    int resIndex = 0;
    int* window = (int*)malloc(k * sizeof(int));
    int windowIndex = 0;

    for (int i = 0; i < k; i++) {
        while (windowIndex > 0 && nums[i] >= nums[window[windowIndex - 1]]) {
            windowIndex--;
        }
        window[windowIndex++] = i;
    }
    res[resIndex++] = nums[window[0]];

    for (int i = k; i < numsSize; i++) {
        if (window[0] == i - k) {
            for (int j = 1; j < windowIndex; j++) {
                window[j - 1] = window[j];
            }
            windowIndex--;
        }
        while (windowIndex > 0 && nums[i] >= nums[window[windowIndex - 1]]) {
            windowIndex--;
        }
        window[windowIndex++] = i;
        res[resIndex++] = nums[window[0]];
    }

    free(window);
    *returnSize = numsSize - k + 1;
    return res;
}