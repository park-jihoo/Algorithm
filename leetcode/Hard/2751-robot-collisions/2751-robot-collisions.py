class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        stack = []
        robots = []
        for i in range(n):
            robots.append({'position': positions[i], 'health': healths[i], 'direction': directions[i], 'original_index': i})
        robots.sort(key=lambda x: x['position'])
        for i in range(n):
            if robots[i]['direction'] == 'L':
                while stack and robots[stack[-1]]['direction'] == 'R' and robots[stack[-1]]['health'] < robots[i]['health']:
                    stack.pop()
                    robots[i]['health'] -= 1
                if not stack or robots[stack[-1]]['direction'] == 'L':
                    stack.append(i) 
                elif stack and robots[stack[-1]]['health'] == robots[i]['health']:
                    stack.pop()  
                elif stack and robots[stack[-1]]['health'] > robots[i]['health']:
                    robots[stack[-1]]['health'] -= 1
            else:
                stack.append(i)
        return [robots[i]['health'] for i in sorted(stack, key=lambda x: robots[x]['original_index'])]