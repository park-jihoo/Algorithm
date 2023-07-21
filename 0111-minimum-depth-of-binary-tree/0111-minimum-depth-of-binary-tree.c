/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode *root) {
  if (root == NULL)
    return 0;
  else if (root->left == NULL && root->right == NULL)
    return 1;
  else if (root->left == NULL)
    return minDepth(root->right) + 1;
  else if (root->right == NULL)
    return minDepth(root->left) + 1;
  else {
    int minLeft = minDepth(root->left);
    int minRight = minDepth(root->right);
    if (minLeft < minRight) {
      return minLeft + 1;
    } else {
      return minRight + 1;
    }
  }
}