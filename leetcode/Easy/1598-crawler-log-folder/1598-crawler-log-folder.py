class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Array String Stack
        folders = []
        for log in logs:
            if len(folders) > 0 and log == "../":
                folders.pop()
            elif log == "./" or log == "../":
                pass
            else:
                folders.append(log)
        return len(folders)
