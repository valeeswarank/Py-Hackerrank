import numpy as np

a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
print("dfdfd")
print(np.array(a, int))
for x in zip(a, b):
    print(x)


# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
languages = ['Java', 'Python', 'JavaScript', 'valee']
versions = [14, 3, 6, 9, 10]

result = zip(languages, versions)
print(list(result))