
from abc import ABC, abstractmethod

from server.common.data import RecommendWord, RequestSearchWord


class AbstractSearchExecutor(ABC):

    @abstractmethod
    def search(self, request_search_word: RequestSearchWord) -> RecommendWord:
        pass
