import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

print(grades_dict)

grades = pd.DataFrame(grades_dict)

print(grades)
grades.index = ["Test1", "Test2", "Test3"]

print(grades)

# To just see Eva's grades
print(grades["Eva"])

# To see Sam's grades
print(grades.Sam)

# not 0 based and will give you the column by name
print(grades.loc['Test1'])

# iloc is 0 based, so [1] will give you second item in the list
print(grades.iloc[1])
"""     Wally Eva Sam Katie Bob
Test1    87   100  94  100   83
Test2    96   87   77   81   65
Test3    70   90   90   82   85
"""

# loc method does include the upper bound
grade.loc['Test1':'Test3']

# iloc method does not include the upper bound because it is 0-based
grade.loc[grades[0:2]]

# To view only test1 and test3
print(grades.loc[['Test1','Test3']])
print(grades.iloc[0,2])

# View only Eva and Katie's grades for Test1 and Test2
print(grades.loc["Test1":"Test2,", ["Eva", "Katie"]])
print(grades.iloc[0:2, [1, 3]])

# Grades above a 90
above_90 = grades[grades > 90]
print(above_90)

# Grades that are a B
b_grades = grades[(grades >= 80) & (grades < 90)]
print(b_grades)

# Look at Eva's test 2 grade
print(grades.at["Test2", "Eva"])
print(grades.iat[1, 2])

# Change Eva's grade to 100
grades.at["Test2", "Eva"] = 100
print(grades)

# Gives us basic information for each column and row of the data
print(grades.describe())

#Set precision to 2 decimal places
pd.set_option('precision', 2))
print(grades.describe())

#Transpose grades by flipping x and y
grades = grades.T
print(grades.describe())
'''OR'''
print(grades.T.describe)

print(grades.T.mean())

grades.sort_index(ascending=False)
print(grades)

#Keep it in ascending order for index and sort by column
grades.sort_index(axis=1)
print(grades)

#sort by the row in descending order
grades.sort_values(by='Test1', axis=1, ascending=False)
print(grades) 