"""
Step 1: Parse through the given array and find "-1"
Step 2: Check previous element and find the next even number if previous element is odd else start with the same 
    number.
Step 3: Generate binary equivalent of decimal numbers
Step 4: Check if odd positions have non-zero numbers; if yes then check for binary of the next even number
Step 5: Replace the appropriate decimal number in the array (for which binary conditions are satisfied)
Step 6: Find the sum of the final array
"""

def binary(num, bin_num):
    if num>=1:
        binary(num//2, bin_num)
    bin_num.append(num%2)


def check_binary(num):
    binary_num = []
    binary(num, binary_num)
    # print(binary_num)
    for i, ele in enumerate(binary_num[::-1]):
        # print('len', len(binary_num))
        if i >= len(binary_num) - 1:
            break
        elif (i+1)%2 == 1:
            if ele != 0:
                # print(f"odd -> {ele}")
                num = check_binary(num+2)
                return num
            else:
                pass
                # print(f"odd -> {ele}")
    return num


def replacer(arr):
    even_gen = 0
    positions_filled = []
    for i, ele in enumerate(arr):
        if ele == -1:
            positions_filled.append(i)
            # Replace
            if arr[i-1] % 2 == 0:
                even_gen = arr[i - 1]
            else:
                even_gen = 2 * ((arr[i - 1] // 2) + 1)
            
            replace_with_num = check_binary(even_gen)
            arr.pop(i)
            arr.insert(i, replace_with_num)
    
    return positions_filled


def get_sum(size_of_array, actual_array):
    pos_arr = replacer(actual_array)
    # if pos_arr:
    #     min_sum = sum_replaced(pos_arr, array)
    min_sum = sum(actual_array)
    print(f"Final Array -> {actual_array}")

    return min_sum


if __name__ == "__main__":
    test_cases = int(input())
    for case in range(test_cases):
        array_size = int(input())
        array = list(map(int, input().strip().split()))

        min_sum = get_sum(array_size, array)
        print(f"Sum for test case {case+1} -> {min_sum}")
