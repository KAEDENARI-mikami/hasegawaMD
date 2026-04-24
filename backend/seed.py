"""
初期データ投入スクリプト（カテゴリとプレースホルダーのみ）
実際のコンテンツはゼミメンバーが追記すること

実行: python seed.py
"""
from database import engine, SessionLocal, Base
from models import Category, Member, Article

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Category).count() == 0:
    db.add_all([
        Category(name="Results", slug="results"),
        Category(name="News", slug="news"),
    ])
    db.commit()
    print("Categories seeded.")

if db.query(Member).count() == 0:
    db.add(Member(
        name="長谷川 教授名",
        role="PROFESSOR",
        bio="自己紹介がここに入ります。",
        research="研究テーマがここに入ります。",
    ))
    db.commit()
    print("Members seeded.")

db.close()
print("Done.")
