def binary_search(input_list, left_pointer, right_pointer, target_value):

    # Check base case
    if left_pointer <= right_pointer:
        # floor division
        mid = (right_pointer + left_pointer) // 2

        # If element is present at the middle itself
        if input_list[mid] == target_value:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif input_list[mid] > target_value:
            return binary_search(
                input_list, left_pointer, mid - 1, target_value
            )

        # Else the element can only be present in right subarray
        else:
            return binary_search(
                input_list, mid + 1, right_pointer, target_value
            )

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
