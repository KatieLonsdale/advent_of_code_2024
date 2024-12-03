# Import necessary library
import numpy as np

# File path
file_path = "./input.txt"

# Load the data from the file
data = np.loadtxt(file_path)

# Split the data into two arrays (columns)
list_1 = data[:, 0]
list_2 = data[:, 1]

list_3 = []

list_1.sort()
list_2.sort()

def compare_lists():
    i = 0
    for number in list_1:
        difference = abs(list_1[i] - list_2[i])
        list_3.append(difference)
        i += 1
        
    return sum_differences(list_3)

def sum_differences(array):
    return sum(array)


print(compare_lists())


