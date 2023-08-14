class Solution {
public:
  bool buddyStrings(string s, string goal) {
    if (s.size() != goal.size())
      return false;
    pair<char, char> difference = {' ', ' '};
    bool multiple = false;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] != goal[i]) {
        if (cnt == 0) {
          difference.first = s[i];
          difference.second = goal[i];
          cnt++;
        } else if (cnt == 1) {
          if (!(difference.first == goal[i] && difference.second == s[i]))
            return false;
          cnt++;
        } else
          return false;
      }
      if (s.find(s[i]) != s.rfind(s[i]))
        multiple = true;
    }

    if (s == goal)
      return multiple;
    return cnt == 2;
  }
};