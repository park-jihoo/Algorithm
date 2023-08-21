class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> anagramGroups;

    for (const auto &s : strs) {
      vector<int> charCount(26, 0);
      for (auto c : s) {
        charCount[c - 'a']++;
      }

      string sRepresentation;
      for (auto count : charCount) {
        sRepresentation += to_string(count) + '#';
      }

      if (anagramGroups.find(sRepresentation) != anagramGroups.end()) {
        anagramGroups[sRepresentation].push_back(s);
      } else {
        anagramGroups[sRepresentation] = {s};
      }
    }

    vector<vector<string>> result;
    for (const auto &kv : anagramGroups) {
      result.push_back(kv.second);
    }

    return result;
  }
};