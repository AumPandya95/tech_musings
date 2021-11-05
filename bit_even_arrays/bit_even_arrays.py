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
            
            # Replace here
            arr.pop(i)
            arr.insert(i, 0)  # replace_with_num
    
    return positions_filled


if __name__ == "__main__":
    test_cases = int(input())
    array_size = int(input())
    array = list(map(int, input().strip().split()))
    pos_arr = replacer(array)
    # if pos_arr:
    #     min_sum = sum_replaced(pos_arr, array)
    min_sum = sum(array)
    print(array)
    print(min_sum)