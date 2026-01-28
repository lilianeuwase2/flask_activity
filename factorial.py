import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def linear_search(n):
    for i in range(n):
        if i == n - 1:
            return i


def bubble_sort(n):
    arr = np.random.randint(0, 100, n)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(n):
    arr = sorted(np.random.randint(0, 100, n))
    target = arr[-1]
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def nested_loops(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def time_complexity_visualizer(algorithm, n_min, n_max, n_step):
    times = []
    input_sizes = list(range(n_min, n_max + 1, n_step))

    for n in input_sizes:
        start = time.time()
        algorithm(n)
        end = time.time()
        times.append(end - start)

    plt.figure()
    plt.plot(input_sizes, times, marker="o")
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Time Complexity Analysis")
    plt.savefig("graph.png")
    plt.close()

    return input_sizes, times
