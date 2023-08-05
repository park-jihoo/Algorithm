/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode left; TreeNode
 * right; TreeNode() {} TreeNode(int val) { this.val = val; } TreeNode(int val, TreeNode left,
 * TreeNode right) { this.val = val; this.left = left; this.right = right; } }
 */
class Solution {
  public List<TreeNode> allPossibleBST(int start, int end, Map<String, List<TreeNode>> memo) {
    List<TreeNode> res = new ArrayList<>();
    if (start > end) {
      res.add(null);
      return res;
    }
    String key = start + "-" + end;
    if (memo.containsKey(key)) {
      return memo.get(key);
    }

    for (int i = start; i <= end; i++) {
      List<TreeNode> left = allPossibleBST(start, i - 1, memo);
      List<TreeNode> right = allPossibleBST(i + 1, end, memo);

      for (TreeNode l : left) {
        for (TreeNode r : right) {
          TreeNode root = new TreeNode(i);
          root.left = l;
          root.right = r;
          res.add(root);
        }
      }
    }

    memo.put(key, res);
    return res;
  }

  public List<TreeNode> generateTrees(int n) {
    Map<String, List<TreeNode>> memo = new HashMap<>();
    return allPossibleBST(1, n, memo);
  }
}
