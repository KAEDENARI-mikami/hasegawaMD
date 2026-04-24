from datetime import datetime
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    slug: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)

    articles: Mapped[list["Article"]] = relationship("Article", back_populates="category")


class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(String(64), nullable=False)
    bio: Mapped[str | None] = mapped_column(Text)
    research: Mapped[str | None] = mapped_column(Text)

    articles: Mapped[list["Article"]] = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    slug: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    summary: Mapped[str | None] = mapped_column(Text)
    content: Mapped[str | None] = mapped_column(Text)
    category_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("categories.id"))
    author_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("members.id"))
    published_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    category: Mapped["Category | None"] = relationship("Category", back_populates="articles")
    author: Mapped["Member | None"] = relationship("Member", back_populates="articles")
