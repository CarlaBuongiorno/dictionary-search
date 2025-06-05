import pytest

from dictionary_search import find_key


@pytest.mark.parametrize('source_dictionary, target_string, expected', [
    ({},                            'key', False),
    ({'key2': 'value'},             'key', False),
    ({'key': 'value'},              'key', True),
    ({'value': 'key'},              'key', False),
    ({'key2': {'key3': 'value'}},   'key', False),
    ({'key2': {'key': 'value'}},    'key', True),
    ({'key1': {'key2': 'value'}, 'key2': {'alpha': 'sausage', 'key': 'value'}},    'key', True),
    ({'key2': {'key4': 'value'}, 'key3': {'key5': {'key6': 'value'}}}, 'key', False),
    ({
        'key2': {
            'key4': 'value'
        }, 
        'key3': {
            'key5': {
                'key6': {
                    'key8': 'value'
                },
                'key7': {
                    'key': 'value'
                }
            }
        }
    },                              'key', True),
])
def test_find_key(source_dictionary, target_string, expected):
    assert find_key(source_dictionary, target_string) == expected
