from datetime import datetime

from src.app.common.data import RequestSearchWord
from src.core.v1.keyword_validator import KeywordValidator


def test_keyword_validator_life_cycle():
    mock_request_search_word = RequestSearchWord(
        request_date=datetime.now(),
        purpose='search similar',
        message='ASAP',
        word='nike',
        num_limit=5,
        request_from='musinsa',
    )

    keyword_validator = KeywordValidator()
    actual = keyword_validator.validate(mock_request_search_word)
    assert isinstance(actual, RequestSearchWord)
