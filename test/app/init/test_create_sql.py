
from src.app.init.create_sql import (
    get_mock_data_set,
    get_random_postfixed_keyword,
    get_random_infixed_keyword,
    get_random_prefixed_keyword,
)


def test_get_random_postfixed_keyword():
    keyword = 'nike'
    postfixed_keyword = get_random_postfixed_keyword(keyword)
    assert isinstance(postfixed_keyword, str)
    assert keyword in postfixed_keyword


def test_get_random_infixed_keyword():
    keyword = 'nike'
    infixed_keyword = get_random_infixed_keyword(keyword)
    assert isinstance(infixed_keyword, str)
    assert keyword in infixed_keyword


def test_get_random_prefixed_keyword():
    keyword = 'nike'
    prefixed_keyword = get_random_prefixed_keyword(keyword)
    assert isinstance(prefixed_keyword, str)
    assert keyword in prefixed_keyword


def test_get_mock_dataset():
    default_mocK_data = {'recommend_word': 'nike'}
    mock_dataset = get_mock_dataset(default_mock_data)

    assert isinstance(mock_dataset, list)
    assert isinstance(mock_dataset[0], dict)
    assert isinstance(mock_dataset[0].keys[0], str)
    assert isinstance(mock_dataset[0].values[0], str)
