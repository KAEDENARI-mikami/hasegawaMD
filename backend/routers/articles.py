from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import Article
from schemas import ArticleOut

router = APIRouter(prefix="/api/articles", tags=["articles"])


@router.get("/", response_model=list[ArticleOut])
def list_articles(
    category: str | None = Query(None),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    q = db.query(Article).options(joinedload(Article.category), joinedload(Article.author))
    if category:
        q = q.join(Article.category).filter_by(slug=category)
    return q.order_by(Article.published_at.desc()).limit(limit).all()


@router.get("/{article_id}", response_model=ArticleOut)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = (
        db.query(Article)
        .options(joinedload(Article.category), joinedload(Article.author))
        .filter(Article.id == article_id)
        .first()
    )
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
