class Solution {
  public int makeArrayIncreasing(int[] arr1, int[] arr2) {
    int m = arr1.length, n = arr2.length;
    if (m == 1) return 0;
    TreeSet<Integer> set = new TreeSet();
    for (int val : arr2) set.add(val);
    // dp[i][j] : for the index of j - 1 in arr1, if we changed i times and then maintain a strickly
    // increasing array from 0 to j , the minimal value for index of j is dp[i][j](we want to make
    // the front numbers as small as possible);
    // if dp[i][j] = Integer.MAX_VALUE, means there is no way to maintain a strictly increasing
    // array with i times from 0 to j.
    // For the last index arr1.length - 1, return the smallest i we can get since it means the
    // minimal steps of change for the whole arr1.
    int[][] dp = new int[m + 1][m + 1];
    for (int i = 0; i <= m; i++) {
      Arrays.fill(dp[i], Integer.MAX_VALUE);
    }
    dp[0][0] = Integer.MIN_VALUE;
    for (int j = 1; j <= m; j++) {
      for (int i = 0; i <= j; i++) {
        if (arr1[j - 1] > dp[i][j - 1]) {
          dp[i][j] = arr1[j - 1];
        }
        if (i > 0 && set.higher(dp[i - 1][j - 1]) != null) {
          dp[i][j] = Math.min(dp[i][j], set.higher(dp[i - 1][j - 1]));
        }
        if (j == m && dp[i][j] != Integer.MAX_VALUE) return i;
      }
    }
    return -1;
  }
}
