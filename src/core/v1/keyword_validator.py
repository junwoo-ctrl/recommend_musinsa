
import arrow

from src.core.interfaces.abstract_keyword_validator import AbstractKeywordValidator as AKValidator
from src.app.common.data import RecommendWord, RequestSearchWord


class KeywordValidator(AKValidator):
    
    def __init__(self):
        self.word: RequestSearchWord = None
        self.kst_tzoffset: int = 540
        self.time_bound: int = 3
        self.purpose: str = 'search similar'
        self.request_from: str = 'musinsa'

    def _validate_request_date(self):
        request_date = arrow.get(self.word.request_date)
        server_date = arrow.utcnow().shift(minutes=self.kst_tzoffset)
        time_interval = (server_date - request_date).total_seconds()

        if time_interval >= self.time_bound:
            # To be implemneted more complex rule.
            print('time bound.')
        return self

    def _validate_purpose(self):
        purpose = self.word.purpose
        if purpose == self.purpose:
            print('statisfy purpose.')
        else:
            raise NotImplementedError(f"Not implemented {purpose} application.")
        return self
            
    def _validate_message(self):
        if self.word.message is not None:
            print('correct message.')
        return self

    def _validate_word(self):
        if self.word.word is not None:
            print('correct word.')
        return self

    def _validate_request_from(self):
        request_from = self.word.request_from
        if request_from == self.request_from:
            print('correct source.')
        return self

    def validate(self, request_search_word: RequestSearchWord) -> RequestSearchWord:
        self.word = request_search_word
        (
            self
            ._validate_request_date()
            ._validate_purpose()
            ._validate_message()
            ._validate_word()
            ._validate_request_from()
        )
        return request_search_word
