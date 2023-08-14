class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        l = [x for x in path.split("/") if not x == ""]
        for i in l:
            if i == ".":
                continue
            elif i == "..":
                if len(answer) > 0:
                    answer.pop()
            else:
                answer.append(i)
        return "/" + "/".join(answer)
