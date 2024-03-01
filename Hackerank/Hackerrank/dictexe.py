#Make a system that track back students names
# and sums their notes

n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
if query_name == name:
        media = student_marks[query_name]
        result = sum(media)/(len(media))
        print(f'{result:.2f}')
