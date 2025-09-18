class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskToUser = {}
        self.taskToPriority = {}
        self.topTask = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskToUser[taskId] = userId
        self.taskToPriority[taskId] = priority
        heapq.heappush(self.topTask, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskToPriority[taskId] = newPriority
        heapq.heappush(self.topTask, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskToUser:
            del self.taskToUser[taskId]
            del self.taskToPriority[taskId]

    def execTop(self) -> int:
        if not self.taskToUser:
            return -1

        while self.topTask:
            priority, negTaskId = heapq.heappop(self.topTask)
            taskId = -negTaskId  
            if taskId in self.taskToPriority and self.taskToPriority[taskId] == -priority:
                user = self.taskToUser.pop(taskId)
                self.taskToPriority.pop(taskId)
                return user

        return -1