from operator import add


def get_commons(input_list: list) -> int:
    # common_likes_index = [_index for _index, number in enumerate(input_list) if int(number)==2]
    # common_dislikes_index = [_index for _index, number in enumerate(input_list) if int(number)==0]
    common_likes_index = []
    common_dislikes_index = []
    # print('inpit_list', len(input_list))
    for _index, number in enumerate(input_list):
        if number == 2:
            common_likes_index.append(_index)
        elif number == 0:
            common_dislikes_index.append(_index)
    # print(common_likes_index)
    return int(len(common_likes_index) + len(common_dislikes_index))


def get_sum_of_list(list_a: list, list_b: list) -> list:
    # return list(np.array(list_a) + np.array(list_b))
    return list(map(add, list_a, list_b))


bob_list = list(map(int, input().strip()))
alice_list = list(map(int, input().strip()))

get_sum = get_sum_of_list(bob_list, alice_list)
# print(get_sum)
common_interests = get_commons(get_sum)

print(common_interests)