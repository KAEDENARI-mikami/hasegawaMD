from datetime import datetime
from pydantic import BaseModel


class CategoryOut(BaseModel):
    id: int
    name: str
    slug: str

    model_config = {"from_attributes": True}


class MemberOut(BaseModel):
    id: int
    name: str
    role: str
    bio: str | None = None
    research: str | None = None

    model_config = {"from_attributes": True}


class ArticleOut(BaseModel):
    id: int
    title: str
    slug: str
    summary: str | None = None
    content: str | None = None
    category: CategoryOut | None = None
    author: MemberOut | None = None
    published_at: datetime | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
