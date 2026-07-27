class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                count = 0
            else: 
                students.append(students[0])
                del students[0]
                count += 1
            if count >= len(students):
                break

        return len(students)