from typing import List
from datetime import datetime

from fastapi import APIRouter
from sklearn.metrics.pairwise import cosine_similarity
from similarity.schemas import PostSimilaritySchema, ResultSchema
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('bert-base-nli-mean-tokens')

router = APIRouter(
    prefix="/similatiry",
    tags=["similarity"],
    responses={404: {"description": "Not found"}},
)

# function which we created before for sentance similarity checking.
@router.post(
    "/calcul",
    response_model=List[ResultSchema],
    responses={403: {"description": "Operation forbidden"}},
    status_code=200
)
def sentence_similarity(data: PostSimilaritySchema):
    sentence_embeddings = model.encode(data.sentence)
    text_embeddings = model.encode(data.texts)

    similarities = cosine_similarity(
        [sentence_embeddings],
        text_embeddings
    )

    results = []
    for t, s in zip(data.texts, similarities[0]):
        results.append({
            "sentence": data.sentence,
            "text": t,
            "similarity": s
        })

    return results