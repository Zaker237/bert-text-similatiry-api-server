from typing import List
from pydantic import BaseModel


class PostSimilaritySchema(BaseModel):
    sentence: str
    texts: List[str]


class ResultSchema(BaseModel):
    sentence: str
    text: str
    similarity: float
