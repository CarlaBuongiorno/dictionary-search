from dictionary_search import find_key


def test_empty_string_in_empty_dict():
    match = find_key({}, '')
    assert match == False


def test_string_in_dict():
    match = find_key({'key': 'value'}, 'key')
    assert match == True


def test_string_not_in_dict():
    match = find_key({'key2': 'value'}, 'key')
    assert match == False


def test_string_in_nested_dict():
    match = find_key({'key2': {'key': 'value'}}, 'key')
    assert match == True


def test_string_not_in_nested_dict():
    match = find_key({'key2': {'key3': 'value'}}, 'key')
    assert match == False