import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def get_sorting_time(arr, sorting_method):
    start_time = time.perf_counter()
    if sorting_method == 'bubble':
        sorted_arr = bubble_sort(arr)
    elif sorting_method == 'selection':
        sorted_arr = selection_sort(arr)
    elif sorting_method == 'insertion':
        sorted_arr = insertion_sort(arr)
    elif sorting_method == 'merge':
        sorted_arr = merge_sort(arr)
    elif sorting_method == 'quick':
        sorted_arr = quick_sort(arr)
    else:
        raise ValueError("Unknown sorting method")

    end_time = time.perf_counter()
    time_taken = end_time - start_time

    return sorted_arr, time_taken


def main():
    # Input numbers from user
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    # Input sorting method from user
    sorting_method = input("Select sorting method (bubble, selection, insertion, merge, quick): ").lower()

    # Get sorted array and time taken
    sorted_arr, time_taken = get_sorting_time(numbers, sorting_method)

    print(f"Sorted Array ({sorting_method.capitalize()} Sort): {sorted_arr}")
    print(f"Time taken: {time_taken:.6f} seconds")


if __name__ == "__main__":
    main()
