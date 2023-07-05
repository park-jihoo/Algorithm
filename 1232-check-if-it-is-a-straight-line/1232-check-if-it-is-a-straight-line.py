class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return 1
        else:
            x = [a[0] for a in coordinates]
            y = [a[1] for a in coordinates]
            if len(x) == x.count(x[0]) or len(y) == y.count(y[0]):
                return 1
            else:
                answer = []
                for i in range(len(coordinates)-1):
                    if(coordinates[i][0]==coordinates[i+1][0] or coordinates[i][1] == coordinates[i+1][1]):
                        return 0
                    answer.append((coordinates[i][0]-coordinates[i+1][0])/(coordinates[i][1]-coordinates[i+1][1]))
                if(len(answer) == answer.count(answer[0])):
                    return 1
                else:
                    return 0
                