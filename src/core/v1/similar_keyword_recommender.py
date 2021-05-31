from typing import List, Dict
from datetime import datetime

from src.core.interfaces.abstract_similar_keyword_recommender import AbstractSimilarKeywordRecommender as AbsKeyRecommend
from src.core.interfaces.abstract_keyword_validator import AbstractKeywordValidator
from src.core.interfaces.abstract_search_executor import AbstractSearchExecutor
from src.core.v1.keyword_validator import KeywordValidator
from src.core.v1.search_executor import DatabaseSearchExecutor
from src.app.common.data import RecommendWord, RequestSearchWord, RecommendResult


class SimilarKeywordRecommender(AbsKeyRecommend):

    def __init__(
        self,
        keyword_validator: AbstractKeywordValidator = KeywordValidator,
        search_executor: AbstractSearchExecutor = DatabaseSearchExecutor,
    ):
        self.keyword_validator: AbstractKeywordValidator = keyword_validator()
        self.search_executor: AbstractSearchExecutor = search_executor

    def search(self, request_search_word: RequestSearchWord) -> List[RecommendWord]:
        request_search_word: RequestSearchWord = self._validate_requested_word(request_search_word)
        recommend_result_list: List[RecommendResult] = self._search(request_search_word)
        recommend_list: List[RecommendWord] = list(map(self._convert_recommend_result, recommend_result_list))
        return recommend_list
 
    def _search(self, request_search_word: RequestSearchWord) -> List[RecommendWord]:
        return self.search_executor.search(request_search_word)
   
    def _validate_requested_word(self, request_search_word: RequestSearchWord) -> RequestSearchWord:
        return self.keyword_validator.validate(request_search_word)

    def _convert_recommend_result(self, recommend_result: RecommendResult) -> RecommendWord:
        recommend = RecommendWord(
            response_date=datetime.now(),
            findby=recommend_result.findby,
            message="success",
            word=recommend_result.word,
        )
        return recommend