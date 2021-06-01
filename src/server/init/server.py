from typing import Optional
from dataclasses import asdict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from clize import run

from server.common.data import RequestSearchWord, RecommendWord
from core.v1.similar_keyword_recommender import SimilarKeywordRecommender


def init_app():
    app = FastAPI()
    return app


app = init_app()


@app.get("/")
async def root():
    return {"message": "hello fast api !!!"}


@app.post("/recommend/")
async def search(request_search_word: RequestSearchWord):
    similar_keyword_recommender = SimilarKeywordRecommender()
    recommend_word: RecommendWord = similar_keyword_recommender.search(request_search_word)
    return recommend_word


if __name__ == "__main__":
    uvicorn.run("src.app.init.server:app", host="0.0.0.0", port=8000, reload=True)
