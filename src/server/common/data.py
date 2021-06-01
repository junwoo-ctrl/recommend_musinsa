from datetime import datetime

from pydantic import BaseModel


class RequestSearchWord(BaseModel):
    request_date: datetime
    purpose: str
    message: str
    word: str
    num_limit: int
    request_from: str


class RecommendWord(BaseModel):
    response_date: datetime
    findby: str
    message: str
    word: str


class RecommendResult(BaseModel):
    findby: str
    word: str

    def __eq__(self, other):
        return self.word == other.word and self.fidnby == other.findby

    def __lt__(self, other):
        return self.word < other.word
