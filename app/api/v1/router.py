"""
API Version 1 Router Aggregator.
Combines all v1 endpoint routers.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health
from app.routers.api_v1.endpoints import (
    ai,
    auth,
    compatibility,
    dna,
    explanation,
    game,
    matchmaking,
    profile,
    riot,
    role_classifier,
    skill_profile,
    squad_recommendation,
    steam_dota,
    survey,
)

api_v1_router = APIRouter()

# Register core v1 endpoints
api_v1_router.include_router(health.router, tags=["Health"])
api_v1_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_v1_router.include_router(profile.router, prefix="/profile", tags=["Gamer Profile"])
api_v1_router.include_router(survey.router, prefix="/survey", tags=["Gamer DNA Survey"])
api_v1_router.include_router(dna.router, prefix="/dna", tags=["Gamer DNA Classification"])
api_v1_router.include_router(role_classifier.router, prefix="/classifier", tags=["Role Classification Engine"])
api_v1_router.include_router(skill_profile.router, prefix="/skills", tags=["Skill Profile Generator"])
api_v1_router.include_router(compatibility.router, prefix="/compatibility", tags=["AI Compatibility Engine"])
api_v1_router.include_router(explanation.router, prefix="/explanation", tags=["AI Explanation Engine"])
api_v1_router.include_router(squad_recommendation.router, prefix="/squads", tags=["Squad Recommendation Engine"])
api_v1_router.include_router(ai.router, prefix="/ai", tags=["FastAPI AI Module"])
api_v1_router.include_router(ai.router, include_in_schema=False)
api_v1_router.include_router(matchmaking.router, prefix="/matchmaking", tags=["Matchmaking Engine"])
api_v1_router.include_router(game.router, prefix="/games", tags=["Game Integration"])
api_v1_router.include_router(steam_dota.router, prefix="/games", tags=["Steam & Dota 2"])
api_v1_router.include_router(riot.router, prefix="/games", tags=["Riot Games"])
