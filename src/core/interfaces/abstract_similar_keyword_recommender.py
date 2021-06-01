
from abc import ABC, abstractmethod

from server.common.data import RecommendWord


class AbstractSimilarKeywordRecommender(ABC):
    
    @abstractmethod
    def search(self) -> RecommendWord:
        pass

    @abstractmethod
    def _validate_requested_word(self):
        pass
