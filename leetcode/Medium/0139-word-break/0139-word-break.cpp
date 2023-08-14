class Solution {
public:
  bool wordBreak(string s, vector<string> &wordDict) {
    queue<int> q;
    q.push(0);
    unordered_set<int> visited;

    while (!q.empty()) {
      int start = q.front();
      q.pop();

      if (start == s.length()) {
        return true;
      }

      for (int end = start + 1; end <= s.length(); ++end) {
        if (visited.find(end) != visited.end()) {
          continue;
        }

        string word = s.substr(start, end - start);
        if (find(wordDict.begin(), wordDict.end(), word) != wordDict.end()) {
          q.push(end);
          visited.insert(end);
        }
      }
    }

    return false;
  }
};
