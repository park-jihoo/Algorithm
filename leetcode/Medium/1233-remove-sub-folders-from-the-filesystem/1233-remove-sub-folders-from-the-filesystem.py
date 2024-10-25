class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans, par = [], ""
        for path in folder:
            if par == "":
                par = path
                ans.append(path)
                continue
            tmp = path.removeprefix(par)
            if tmp != path and tmp[0] == "/":
                continue
            else:
                par = path
                ans.append(path)
        return ans
