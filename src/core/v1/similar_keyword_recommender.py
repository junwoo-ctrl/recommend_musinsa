from typing import List, Dict
from datetime import datetime

from core.interfaces.abstract_similar_keyword_recommender import AbstractSimilarKeywordRecommender as AbsKeyRecommend
from core.interfaces.abstract_keyword_validator import AbstractKeywordValidator
from core.interfaces.abstract_search_executor import AbstractSearchExecutor
from core.v1.keyword_validator import KeywordValidator
from core.v1.search_executor import DatabaseSearchExecutor
from app.common.data import RecommendWord, RequestSearchWord, RecommendResult
from app.util.logger import RecommendLogger as Logger


class SimilarKeywordRecommender(AbsKeyRecommend):

    def __init__(
        self,
        keyword_validator: AbstractKeywordValidator = KeywordValidator,
        search_executor: AbstractSearchExecutor = DatabaseSearchExecutor,
    ):
        self.keyword_validator: AbstractKeywordValidator = keyword_validator()
        self.search_executor: AbstractSearchExecutor = search_executor
        self.logger = Logger(__name__)

    def search(self, request_search_word: RequestSearchWord) -> List[RecommendWord]:
        request_search_word: RequestSearchWord = self._validate_requested_word(request_search_word)
        recommend_result_list: List[RecommendResult] = self._search(request_search_word)
        recommend_list: List[RecommendWord] = list(map(self._convert_recommend_result, recommend_result_list))
        self.logger.info("successfully get all recommend words by service.")
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
