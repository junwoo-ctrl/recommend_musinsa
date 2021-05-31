
from abc import ABC, abstractmethod

from src.app.common.data import RecommendWord, RequestSearchWord


class AbstractSearchExecutor(ABC):

    @abstractmethod
    def search(self, request_search_word: RequestSearchWord) -> RecommendWord:
        pass
