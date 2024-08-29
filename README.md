# Flat Generator and Flat Iterator

This project contains two implementations for flattening nested lists:

1. flat_generator: A generator function that recursively flattens a list of lists.
2. FlatIterator: An iterator class that flattens a list of lists.

## Usage

1. Import the flat_generator function and the FlatIterator class from the script.
2. Use the flat_generator function to flatten a list of lists:

nested_list = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

for item in flat_generator(nested_list):
    print(item)

3. Use the FlatIterator class to flatten a list of lists:

nested_list = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

flat_iterator = FlatIterator(nested_list)
for item in flat_iterator:
    print(item)

## Testing

The script includes two test functions, test_4() for the flat_generator function and test_3() for the FlatIterator class. You can run these tests to ensure the correctness of the implementations.

## Requirements

- Python 3.x

## License

This project is licensed under the [MIT License](LICENSE).

README.md (Russian)

# Плоский генератор и плоский итератор

Этот проект содержит две реализации для плоской трансформации вложенных списков:

1. flat_generator: Функция-генератор, рекурсивно сглаживающая список списков.
2. FlatIterator: Класс итератора, сглаживающий список списков.

## Использование

1. Импортируйте функцию flat_generator и класс FlatIterator из скрипта.
2. Используйте функцию flat_generator для плоской трансформации списка списков:

nested_list = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

for item in flat_generator(nested_list):
    print(item)

3. Используйте класс FlatIterator для плоской трансформации списка списков:

nested_list = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

flat_iterator = FlatIterator(nested_list)
for item in flat_iterator:
    print(item)

## Тестирование

Скрипт включает две тестовые функции, test_4() для функции flat_generator и test_3() для класса FlatIterator. Вы можете запустить эти тесты, чтобы убедиться в правильности реализаций.

## Требования

- Python 3.x

## Лицензия

Этот проект распространяется под [Лицензией MIT](LICENSE).
