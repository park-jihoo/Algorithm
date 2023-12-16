class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size())
      return false;
    multiset<char> s_set;
    multiset<char> t_set;
    for (int i = 0; i < s.size(); i++) {
      s_set.insert(s[i]);
      t_set.insert(t[i]);
    }
    return s_set == t_set;
  }
};