import numpy as np

# a = np.array([100,150])
# p = np.percentile(a,50)

# print(p)

# .venv\Scripts\activate


class Students(object):
    def __init__(self, name, classs, scor):
        self.name = name
        self.classs = classs
        self.scor = scor
        # Calculate the 50th percentile (median) within the constructor.
        self.median_score = np.percentile(scor, 50) if scor else None #Handle empty score lists

# Example usage:
scores1 = [60, 33, 45, 38, 50]
student1 = Students("Yashpalsinh", "10th", scores1)

print(f"Student: {student1.name}")
print(f"Class: {student1.classs}")
print(f"Scores: {student1.scor}")
print(f"Median Score: {student1.median_score}")

scores2 = [12,]
student2 = Students("Jane Doe", "11th", scores2)
print(f"Student: {student2.name}")
print(f"Scores: {student2.scor}")
print(f"Median Score: {student2.median_score}")