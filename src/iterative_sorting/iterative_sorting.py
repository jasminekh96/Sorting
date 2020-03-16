# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        if smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted_nums = [*arr]
    while True:
        swapped = False

        for i in range(0, len(sorted_nums)-1):
            if sorted_nums[i] > sorted_nums[i+1]:
                greater = sorted_nums[i]
                lesser = sorted_nums[i+1]

                sorted_nums[i] = lesser
                sorted_nums[i+1] = greater

                swapped = True
            if not swapped: 
                break
    return sorted_nums

# # Another way to do bubble sort from google
# def bubble_sort( arr ):
#     has_swapped = True

#     num_of_iterations = 0

#     while(has_swapped):
#         has_swapped = False
#         for i in range(len(arr) - num_of_iterations - 1):
#             if arr[i] > arr[i+1]:
#                 # Swap
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 has_swapped = True
#         num_of_iterations += 1
#     return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

