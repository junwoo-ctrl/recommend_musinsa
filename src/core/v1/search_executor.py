import random
from typing import List, Any

from core.interfaces.abstract_search_executor import AbstractSearchExecutor
from core.v1.query_manager import QueryManager
from app.common.data import RecommendWord, RequestSearchWord, RecommendResult
from app.util.tools import EnvTool
from app.util.logger import RecommendLogger as Logger


class DatabaseSearchExecutor(AbstractSearchExecutor):
    logger = Logger(__name__)
    
    @staticmethod
    def search(request_search_word: RequestSearchWord) -> List[RecommendResult]:
        num_limit_word: int = request_search_word.num_limit
        search_word_string: str = request_search_word.word

        provided_words: List[List[RecommendResult]] = DatabaseSearchExecutor._search_query_to_db(search_word_string)
        recommend_list: List[RecommendResult] = DatabaseSearchExecutor._rearrange_recommend_list(provided_words, num_limit_word)
        return recommend_list

    @staticmethod
    def _search_query_to_db(search_word: str) -> List[List[RecommendResult]]:
        prefix_recommend = PrefixRecommendProvider.provide(search_word)
        infix_recommend = InfixRecommendProvider.provide(search_word)
        postfix_recommend = PostfixRecommendProvider.provide(search_word)
        ngram_recommend = NgramRecommendProvider.provide(search_word)
        resultset = [
            prefix_recommend,
            infix_recommend,
            postfix_recommend,
            ngram_recommend,
        ]

        DatabaseSearchExecutor.logger.info("successfully find recommend word list!")
        return resultset

    @staticmethod
    def _rearrange_recommend_list(provided_words: List[List[RecommendResult]], num_limit_word: int) -> List[RecommendResult]:
        all_recommended = sorted([ele2 for ele in provided_words for ele2 in ele])
        DatabaseSearchExecutor.logger.info(f"get only limited number of {num_limit_word} word!")
        return all_recommended


# Todo: refactor
class PrefixRecommendProvider:
    findby: str = 'findby prefix pattern'
    logger = Logger(__name__)
    prefix_query_string = """
        SELECT id, recommend_word
        FROM {env}.recommend_store
        WHERE recommend_word LIKE '{search_word}%';
    """
    
    @staticmethod
    def provide(search_word: str) -> List[RecommendResult]:
        statement = PrefixRecommendProvider.prefix_query_string.format(
            env=EnvTool.get_env(),
            search_word=search_word,
        )
        query_resultset: List[str] = [r['recommend_word'] for r in QueryManager.query(statement)]
        query_resultset: List[RecommendResult] = [PrefixRecommendProvider._convert_to_obj(r) for r in query_resultset]
        PrefixRecommendProvider.logger.info(f"successfully get recommend words {PrefixRecommendProvider.findby}.")
        return query_resultset

    @staticmethod
    def _convert_to_obj(query_result: str) -> RecommendResult:
        recommend_result = RecommendResult(
            findby=PrefixRecommendProvider.findby,
            word=query_result,
        )
        return recommend_result


class PostfixRecommendProvider:
    findby: str = "findby postfix pattern"
    logger = Logger(__name__)
    postfix_query_string = """
        SELECT id, recommend_word
        FROM {env}.recommend_store
        WHERE recommend_word LIKE '%{search_word}';
    """
    
    @staticmethod
    def provide(search_word: str) -> List[RecommendResult]:
        statement = PostfixRecommendProvider.postfix_query_string.format(
            env=EnvTool.get_env(),
            search_word=search_word,
        )
        query_resultset: List[str] = [r['recommend_word'] for r in QueryManager.query(statement)]
        query_resultset: List[RecommendResult] = [PostfixRecommendProvider._convert_to_obj(r) for r in query_resultset]
        PostfixRecommendProvider.logger.info(f"successfully get recommend words {PostfixRecommendProvider.findby}.")
        return query_resultset

    @staticmethod
    def _convert_to_obj(query_result: str) -> RecommendResult:
        recommend_result = RecomendResult(
            findby=PostfixRecommendProvider.findby,
            word=query_result,
        )
        return recommend_result


class InfixRecommendProvider:
    findby: str = "findby infix pattern"
    logger = Logger(__name__)
    infix_query_string = """
        SELECT id, recommend_word
        FROM {env}.recommend_store
        WHERE recommend_word LIKE '%{search_word}%';
    """
    
    @staticmethod
    def provide(search_word: str) -> List[RecommendResult]:
        statement = InfixRecommendProvider.infix_query_string.format(
            env=EnvTool.get_env(),
            search_word=search_word,
        )
        query_resultset: List[str] = [r['recommend_word'] for r in QueryManager.query(statement)]
        query_resultset: List[RecommendResult] = [InfixRecommendProvider._convert_to_obj(r) for r in query_resultset]
        InfixRecommendProvider.logger.info(f"successfully get recommend words {InfixRecommendProvider.findby}.")
        return query_resultset

    @staticmethod
    def _convert_to_obj(query_result: str) -> RecommendResult:
        recommend_result = RecommendResult(
            findby=InfixRecommendProvider.findby,
            word=query_result,
        )
        return recommend_result


class NgramRecommendProvider:
    findby: str = "findby ngram pattern"
    logger = Logger(__name__)
    ngram_query_string = """
        SELECT *
        FROM {env}.recommend_store
        WHERE MATCH recommend_word AGAINST ('{search_word}' IN NATURAL LANGUAGE MODE);
    """
    
    @staticmethod
    def provide(search_word: str) -> List[RecommendResult]:
        statement = NgramRecommendProvider.ngram_query_string.format(
            env=EnvTool.get_env(),
            search_word=search_word,
        )
        query_resultset: List[str] = [r['recommend_word'] for r in QueryManager.query(statement)]
        query_resultset: List[RecommendResult] = [NgramRecommendProvider._convert_to_obj(r) for r in query_resultset]
        NgramRecommendProvider.logger.info(f"successfully get recommend words {NgramRecommendProvider.findby}.")
        return query_resultset

    @staticmethod
    def _convert_to_obj(query_result: str) -> RecommendResult:
        recommend_result = RecommendResult(
            findby=NgramRecommendProvider.findby,
            word=query_result,
        )
        return recommend_result
