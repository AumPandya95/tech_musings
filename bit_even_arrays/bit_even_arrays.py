def check_binary(num):
    binary_num = []
    # Convert num to binary
    print(binary_num)
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