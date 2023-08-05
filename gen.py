import types

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Testing flat_generator:")
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
        print(f"Expected: {check_item}, Got: {flat_iterator_item}")

    result_list = list(flat_generator(list_of_lists_2))
    expected_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert result_list == expected_list

    print("Expected List: ", expected_list)
    print("Result List:   ", result_list)
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print("Test passed successfully!")


if __name__ == '__main__':
    test_4()
