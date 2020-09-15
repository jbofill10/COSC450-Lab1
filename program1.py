import random
'''
Author: Juan Bofill
Description: Takes input of an array or generates a random array and does quicksort on it
'''
def run_quicksort(arr):
    if len(arr) <= 1: return arr
    return run_quicksort([l for l in arr[1:] if l < arr[0]]) + arr[0:1] + run_quicksort([h for h in arr[1:] if h >= arr[0]])

if __name__ == "__main__":
    arr = input("Type in custom array (Ex: 3 5 2 5) or leave blank for a random array: ")

    if len(arr) < 1:
        length = random.randint(10,20)

        arr = [random.randint(0,100) for _ in range(length)]
        print("Randomly Generated Array: \n", arr)
    else:
        arr = [int(num) for num in arr.split(" ")]
        print("Your custom array: \n", arr)

    sorted_arr = run_quicksort(arr)
    print("Sorted Array: \n", sorted_arr)