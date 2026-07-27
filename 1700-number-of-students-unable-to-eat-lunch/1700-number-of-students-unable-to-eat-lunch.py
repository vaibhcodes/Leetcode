class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = len(sandwiches)
        sandwichq = deque(sandwiches)
        q = deque(students)
        while sandwichq and counter > 0:
            student = q.popleft()
            counter -= 1
            if sandwichq[0] == student:
                sandwichq.popleft()
                counter = len(sandwichq)
            else:
                q.append(student)
        
        return len(sandwichq)