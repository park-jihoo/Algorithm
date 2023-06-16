class Solution {
    int mod = (int) 1e9 + 7;
    
    public int numOfWays(int[] nums) {
        int n = nums.length;
        long[][] comb = getComb(n);
        return (int) ((helper(nums, comb) - 1) % mod);
    }
    
    private long helper(int[] nums, long[][] comb) {
        if (nums.length <= 2) return 1;
        int root = nums[0];
        List<Integer> l = new ArrayList();
        List<Integer> r = new ArrayList();
        for (int i = 1; i < nums.length; i ++) {
            int val = nums[i];
            if (val < root) {
                l.add(val);
            } else {
                r.add(val);
            }
        }
        int[] left = l.stream().mapToInt(i -> i).toArray();
        int[] right = r.stream().mapToInt(i -> i).toArray();
        long lways = helper(left, comb) % mod;
        long rways = helper(right, comb) % mod;
        return (((comb[left.length + right.length][left.length] * lways) % mod) * rways) % mod;
    }
    
    private long[][] getComb(int n) {
        long[][] comb = new long[n + 1][n + 1];
        for (int i = 1; i <= n; i ++) {
            for (int j = 0; j <= i; j ++) {
                if (j == 0 || i == j) {
                    comb[i][j] = 1;
                } else {
                    comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;
                }
            }
        }
        return comb;
    }
}