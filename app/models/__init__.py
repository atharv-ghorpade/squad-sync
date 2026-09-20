"""
SQLAlchemy Models Package.
Exports all 6 core models for centralized access and Alembic autogenerate discovery:
1. User (users)
2. GamerProfile (gamer_profiles)
3. GameAccount (game_accounts)
4. PlayerStat (player_stats)
5. SurveyAnswer (survey_answers)
6. GamerDNA (gamer_dna)
"""

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin
from app.models.game_account import GameAccount
from app.models.gamer_dna import GamerDNA
from app.models.gamer_profile import GamerProfile
from app.models.player_stat import PlayerStat
from app.models.survey_answer import SurveyAnswer, SurveyResponse
from app.models.user import User

__all__ = [
    "Base",
    "TimestampMixin",
    "UUIDPrimaryKeyMixin",
    "User",
    "GamerProfile",
    "GameAccount",
    "PlayerStat",
    "SurveyAnswer",
    "SurveyResponse",
    "GamerDNA",
]
