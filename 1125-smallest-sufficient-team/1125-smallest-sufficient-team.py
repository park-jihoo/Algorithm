class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp = {0:[]}
        key = {value:idx for idx, value in enumerate(req_skills)}
        for idx, p in enumerate(people):
            current_skill = 0
            for skill in p:
                current_skill |= 1 << key[skill]

            for skill_set, members in dict(dp).items():
                total_skill = skill_set|current_skill
                if total_skill == skill_set:
                    continue
                if total_skill not in dp or len(dp[total_skill])>len(members)+1:
                    dp[total_skill] = members + [idx]
        return dp[(1<<len(req_skills)) - 1]