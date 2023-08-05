class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = [(list_of_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            lst, col = self.stack[-1]
            if col >= len(lst):
                self.stack.pop()
                continue

            item = lst[col]
            self.stack[-1] = (lst, col + 1)

            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                return item

        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Testing FlatIterator:")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
        print(f"Expected: {check_item}, Got: {flat_iterator_item}")

    result_list = list(FlatIterator(list_of_lists_2))
    expected_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert result_list == expected_list

    print("Expected List: ", expected_list)
    print("Result List:   ", result_list)
    print("Test passed successfully!")


if __name__ == '__main__':
    test_3()
