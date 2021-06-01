
from app.common.data import RecommendResult, RequestSearchWord
from core.v1.search_executor import (
    SearchExecutor,
    PrefixRecommendProvider,
    InfixRecommendProvider,
    PostfixRecommendProvier,
    NgramfixRecommendProvider,
)


def test_prefix_recommend_provide():
    mock_search_word = 'nike'
    
    actual = PrefixRecommendProvider.provide(mock_search_word)
    assert isinstance(actual, list)
    assert len(actual) >= 0

    for element in actual:
        assert isinstance(element, RecommendResult)


def test_postfix_recommend_provide():
    mock_search_word = 'nike'

    actual = PostfixRecommendProvider.provide(mock_search_word)
    assert isinstance(actual, list)
    assert len(actual) >= 0

    for element in actual:
        assert isinstance(element, RecommendResult)


def test_infix_recommend_provide():
    mock_search_word = 'nike'

    actual = InfixRecommendProvider.provide(mock_search_word)
    assert isinstance(actual, list)
    assert len(actual) >= 0

    for element in actual:
        assert isinstance(element, RecommendResult)


def test_ngramfix_recommend_provide():
    mock_search_word = 'nike'

    actual = NgramRecommendProvider.provide(mock_search_word)
    assert isinstance(actual, list)
    assert len(actual) >= 0

    for element in actual:
        assert isinstance(element, RecommendResult)


def test_simple_obj_convert():
    
    # simple mocking query resultset
    mock_query_result = ['abcdnike']

    # prefix provider -> obj
    actual_recommend_result = PrefixRecommendProvider._convert_to_obj(mock_query_result)
    assert isinstance(actual_recommend, RecommendResult)
    assert RecommendResult.findby == 'findby prefix pattern'

    # postfix provider -> obj
    actual_recommend_result = PostfixRecommendProvider._convert_to_obj(mock_query_result)
    assert isinstance(actual_recommend, RecommendResult)
    assert RecommendResult.findby == 'findby postfix pattern'

    # infix provider -> obj
    actual_recommend_result = InfixRecommendProvider._convert_to_obj(mock_query_result)
    assert isinstance(actual_recommend, RecommendResult)
    assert RecommendResult.findby == 'findby infix pattern'

    # ngram provider -> obj
    actual_recommend_result = NgramfixRecommendProvider._convert_to_obj(mock_query_result)
    assert isinstance(actual_recommend, RecommendResult)
    assert RecommendResult.findby == 'findby ngram pattern'


def test_database_search_executor_lifecyle():
    mock_request_search_word = RequestSearchWord(
        request_date=datetime.now(),
        purpose='search similar',
        message='ASAP',
        num_limit=5,
        request_from='musinsa',
    )

    actual_recommend_list = DatabaseSearchExecutor.search(mock_request_search_word)
    assert isinstance(actual_recommend_list, list)
    assert isinstance(actual_recommend_list[0], RecommendResult)

    mock_single_recommend_result = actual_recommend_list[0]
    if mock_single_recommend_result is not None:
        assert mock_single_recommend_result.findby is not None
        assert mock_single_recommend_result.word is not None
