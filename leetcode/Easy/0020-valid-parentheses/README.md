<h2><a href="https://leetcode.com/problems/valid-parentheses/">20. Valid Parentheses</a></h2><h3>Easy</h3><hr>Can you solve this real interview question? Valid Parentheses - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.
 3. Every close bracket has a corresponding open bracket of the same type.

 

Example 1:


Input: s = "()"
Output: true


Example 2:


Input: s = "()[]{}"
Output: true


Example 3:


Input: s = "(]"
Output: false


 

Constraints:

 * 1 <= s.length <= 104
 * s consists of parentheses only '()[]{}'.