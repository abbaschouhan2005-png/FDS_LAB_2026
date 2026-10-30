'''name - abbas chouhan
roll no - 256502002
batch - Ai&Ml
3 semester , 2 Year
Day 1 Assignment 1'''
import numpy as np
rng = np.random.default_rng()
marks = rng.integers(0, 101, size=(4, 5))
total_marks = np.sum(marks, axis=1)
percentage = (total_marks / (5 * 100)) * 100
print("Marks Matrix:")
print(marks)
print("\nTotal Marks of Each Student:")
print(total_marks)
print("\nPercentage of Each Student:")
print(percentage)
average_marks = np.mean(marks, axis=0)
std_deviation = np.std(marks, axis=0)
print("Marks Matrix (4 Students × 5 Subjects):")
print(marks)
print("\nAverage Marks in Each Subject:")
print(average_marks)
print("\nStandard Deviation in Each Subject:")
print(std_deviation)
2. import numpy as np
rng = np.random.default_rng()
marks = rng.integers(0, 101, size=(4, 5))
highest_marks = np.max(marks, axis=0)
student_index = np.argmax(marks, axis=0)
print("Marks Matrix (4 Students × 5 Subjects):")
print(marks)
print("\nHighest Marks in Each Subject:")
print(highest_marks)
print("\nIndex of Student Scoring Highest Marks in Each Subject:")
print(student_index)
print("\nStudent Number (1-based indexing):")
print(student_index + 1)
import numpy as np
rng = np.random.default_rng()
marks = rng.integers(0, 101, size=(4, 5))
pass_mask = marks >= 40
print("Marks Matrix (4 Students × 5 Subjects):")
print(marks)
print("\nBoolean Mask (True = Pass, False = Fail):")
print(pass_mask)
print("\nPass/Fail Status:")
print(np.where(pass_mask, "Pass", "Fail"))