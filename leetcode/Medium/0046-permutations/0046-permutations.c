/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void backtrack(int **result, int *nums, int numsSize, int start, int *returnSize) {
    if (start == numsSize - 1) {
        result[*returnSize] = (int *)malloc(numsSize * sizeof(int));
        for (int i = 0; i < numsSize; i++) {
            result[*returnSize][i] = nums[i];
        }
        (*returnSize)++;
    } else {
        for (int i = start; i < numsSize; i++) {
            swap(&nums[start], &nums[i]);
            backtrack(result, nums, numsSize, start + 1, returnSize);
            swap(&nums[start], &nums[i]);  // Backtrack
        }
    }
}

int **permute(int *nums, int numsSize, int *returnSize, int **returnColumnSizes) {
    *returnSize = 0;
    int totalPermutations = 1;
    for (int i = 1; i <= numsSize; i++) {
        totalPermutations *= i;
    }
    
    int **result = (int **)malloc(totalPermutations * sizeof(int *));
    *returnColumnSizes = (int *)malloc(totalPermutations * sizeof(int));

    backtrack(result, nums, numsSize, 0, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    return result;
}