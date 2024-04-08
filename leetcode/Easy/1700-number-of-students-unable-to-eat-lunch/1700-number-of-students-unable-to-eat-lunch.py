class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = deque(sandwiches)
        cont = 0
        while stack and queue and cont < len(stack):
            prefer = queue.popleft()
            if stack[0] == prefer:
                stack.popleft()
                cont = 0
            else:
                queue.append(prefer)
                cont += 1
        return len(stack)