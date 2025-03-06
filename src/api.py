from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.model import (
    recommend_movies,
)  # Import using full package path  # Import the recommendation function

app = FastAPI()


# Request model for user input
class RecommendationRequest(BaseModel):
    user_id: int
    num_recommendations: int = 5


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}


# Recommendation endpoint


@app.get("/recommend/{movie_name}")
def recommend(movie_name: str):
    recommendations = recommend_movies(movie_name)
    return {"recommended_movies": recommendations}
