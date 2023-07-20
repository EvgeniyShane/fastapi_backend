from fastapi import FastAPI, HTTPException
from models import User, Article
from database import db_users, db_articles

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User):
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="A user already exists")
    db_users[user.username] = user
    return user

@app.get("/users/{username}", response_model=User)
def read_user(username: str):
    if username not in db_users:
        raise HTTPException(status_code=404, detail="User is not found")
    return db_users[username]

@app.post("/articles/", response_model=Article)
def create_article(article: Article):
    article_id = len(db_articles) + 1
    db_articles[article_id] = article
    return {"article_id": article_id, **article.dict()}

@app.get("/articles/{article_id}", response_model=Article)
def read_article(article_id: int):
    if article_id not in db_articles:
        raise HTTPException(status_code=404, detail="Article not foundа")
    return db_articles[article_id]