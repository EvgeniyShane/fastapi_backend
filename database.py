from typing import Dict

from models import User, Article

db_users: Dict[str, User] = {}
db_articles: Dict[int, Article] = {}