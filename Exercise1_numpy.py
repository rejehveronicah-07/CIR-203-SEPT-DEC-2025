import numpy as np

transactions = np.array([
    [1200, 1300, 1400, 1500, 1600, 1700],
    [1100, 1150, 1200, 1250, 1300, 1350],
    [2000, 2100, 2200, 2300, 2400, 2500],
    [900, 1000, 1100, 1200, 1300, 1400]
])

total_per_branch = transactions.sum(axis=1)
print(total_per_branch)

highest_branch = np.argmax(total_per_branch) + 1
print(highest_branch)

average_volume = transactions.mean()
print(average_volume)

reshaped_array = transactions.reshape(3, 8)
print(reshaped_array)
print("Reshaping groups data differently but does not change total values.")
