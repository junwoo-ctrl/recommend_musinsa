
from typing import Dict, Union
from abc import ABC, abstractmethod

from app.common.data import RequestSearchWord


class AbstractKeywordValidator:
    
    @abstractmethod
    def validate(self, request_search_word: RequestSearchWord) -> RequestSearchWord:
        pass

    @abstractmethod
    def _validate_request_date(self, request_search_word: RequestSearchWord) -> Union[str, RequestSearchWord]:
        pass

    @abstractmethod
    def _validate_purpose(self, request_search_word: RequestSearchWord) -> Union[str, RequestSearchWord]:
        pass

    @abstractmethod
    def _validate_message(self, request_search_word: RequestSearchWord) -> Union[str, RequestSearchWord]:
        pass

    @abstractmethod
    def _validate_word(self, request_search_word: RequestSearchWord) -> Union[str, RequestSearchWord]:
        pass

    @abstractmethod
    def _validate_request_form(self) -> Dict[str, Union[RequestSearchWord, bool]]:
        pass



