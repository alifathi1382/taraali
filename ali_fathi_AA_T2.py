import numpy as np
import time


def max_subarray(arr):
    n = len(arr)
    max_sum = int()
    start_idx = 0
    end_idx = 0

    for i in range(n):
        for j in range(i, n):
            current_sum = 0

            for k in range(i, j + 1):
                current_sum += arr[k]
            if current_sum > max_sum:
                max_sum = current_sum
                start_idx = i
                end_idx = j

    print("The largest subarray:", arr[start_idx:end_idx + 1])
    print("The max sum:", max_sum)


start_time = time.time()
a = np.random.randint(-9, +9, 100)
print(a)
max_subarray(a)
print("---%s seconds ---" % (time.time() - start_time))
