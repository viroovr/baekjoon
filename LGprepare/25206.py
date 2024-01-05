grades = ["A+", 'A0', "B+", "B0", "C+", 'C0', 'D+', 'D0', 'F']
grade_table = {v: 4.5 - i * 0.5 for i, v in enumerate(grades)}
grade_table['F'] = 0.0
sum_mul = 0
sum_credit = 0
for _ in range(20):
    _, credit, grade = input().split()
    if grade == 'P':
        continue
    credit = float(credit)
    sum_mul += credit * grade_table[grade]
    sum_credit += credit
print(sum_mul / sum_credit)