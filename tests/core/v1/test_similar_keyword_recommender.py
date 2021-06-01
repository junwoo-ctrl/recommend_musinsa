from datetime import datetime

from core.v1.similar_keyword_recommender import SimilarKeywordRecommender
from server.common.data import RecommendWord, RequestSearchWord, RecommendResult


def test_search_similar_keyword():
    mock_request_search_word = RequestSearchWord(
        request_date=datetime.now(),
        purpose='search similar',
        message='ASAP',
        word='nike',
        num_limit=5,
        request_from='musinsa',
    )

    similar_keyword_recommender = SimilarKeywordRecommender()
    actual_recommend_list = similar_keyword_recommender.search(mock_request_search_word)
    
    assert isinstance(actual_recommend_list, list)
    assert isinstance(actual_recommend_list[0], RecommendWord)


def test_convert_recommend_result():
    mock_recommend_result = RecommendResult(
        findby="findby infix pattern",
        word="isnikegood",
    )

    actual_recommend_word = SimilarKeywordRecommender._convert_recommend_result(mock_recommend_result)
    assert isinstance(actual_recommend_word, RecommendWord)
