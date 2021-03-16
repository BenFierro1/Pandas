import pandas as pd

# create a 1-D array anc can do the same using the range function
grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))

print(grades)

a = grades[0]
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

# calling Series method describe produces all these stats and more:
grades.describe()

grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])
print(grades)


# If you initialize a Series with a dictionary, its keys become the
# Series' indices, and its values become the Series' element values:

grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

# you can access individual elements via square brackets
# containing a custom index value:
print(grades["Eva"])
# 100

# If the custom indices are strings that could represent valid python identifiers,
# pandas automatically add them to the Series as attributes that you can access via a doe(.), as in:
grades.Wally
# 87

# Series also has built-in attributes. For example, the dtype attribute returns
# the underlying array's element type:
grades.dtype
# dtype('int64')

grades.values
# array([87, 100, 94])

""" 0 Hammer
    1   Saw
    2 Wrentch
    dtype: object"""

# answer = hardware.str.contains("a")

# print(answer)

# hardware_upper = hardware.str.hardware_upper()

# print(hardware_upper)
