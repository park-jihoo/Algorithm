/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  int minDepth(TreeNode *root) {
    if (root == nullptr)
      return 0;
    else if (root->left == nullptr && root->right == nullptr)
      return 1;
    else if (root->left == nullptr)
      return minDepth(root->right) + 1;
    else if (root->right == nullptr)
      return minDepth(root->left) + 1;
    else {
      int minLeft = minDepth(root->left);
      int minRight = minDepth(root->right);
      return min(minLeft, minRight) + 1;
    }
  }
};