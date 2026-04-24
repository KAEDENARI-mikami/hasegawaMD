# 要件定義書 — 長谷川ゼミ公式サイト

## 1. プロジェクト概要

| 項目 | 内容 |
|------|------|
| 名称 | 長谷川ゼミ公式Webサイト |
| 目的 | ゼミ紹介・研究成果発表のオンラインプラットフォーム |
| 対象ユーザー | 在学生、受験予定者、一般閲覧者、ゼミメンバー |

---

## 2. ページ構成

| ページ | パス | 概要 |
|--------|------|------|
| ホーム | `/` | ゼミのキャッチコピー・最新成果・お知らせの概要表示 |
| ゼミ紹介 | `/about` | ゼミの理念・研究分野・活動内容 |
| 成果発表 | `/results` | 研究成果・論文・発表資料の一覧 |
| メンバー | `/members` | 教員・学生メンバー紹介 |
| ニュース | `/news` | お知らせ・イベント一覧 |
| 詳細ページ | `/results/:id` `/news/:id` | 各コンテンツの詳細 |

---

## 3. 機能要件

### フロントエンド
- [ ] SPA（Single Page Application）によるページ遷移
- [ ] レスポンシブデザイン（モバイル対応）
- [ ] 記事カード一覧表示
- [ ] 記事詳細表示（Markdown対応予定）
- [ ] メンバー一覧・プロフィール表示
- [ ] カテゴリフィルタリング

### バックエンド API
- [ ] `GET /api/articles` — 成果・ニュース記事一覧取得
- [ ] `GET /api/articles/{id}` — 記事詳細取得
- [ ] `GET /api/members` — メンバー一覧取得
- [ ] `GET /api/categories` — カテゴリ一覧取得
- [ ] CORS設定（フロントエンドからのアクセス許可）

### データベース
- [ ] articles テーブル（記事管理）
- [ ] members テーブル（メンバー管理）
- [ ] categories テーブル（カテゴリ管理）

---

## 4. 非機能要件

| 項目 | 内容 |
|------|------|
| デザイン方針 | WIRED.jp 参考。モノトーン・エディトリアル・フラットデザイン |
| フォント | Helvetica Neue + 游ゴシック（本文）、モノスペース（ラベル） |
| カラー | Black `#000`、White `#fff`、Body text `#1a1a1a`、Meta `#757575` |
| パフォーマンス | SPA + REST API構成、初回ロード最適化 |

---

## 5. 技術スタック

| レイヤー | 技術 |
|----------|------|
| フロントエンド | Vue 3 + Vite + Vue Router |
| バックエンド | Python 3.12 + FastAPI |
| データベース | SQLite（開発）/ PostgreSQL（本番移行予定） |
| ORM | SQLAlchemy |
| バリデーション | Pydantic v2 |

---

## 6. ディレクトリ構成

```
hase2026/
├── frontend/          # Vue.js フロントエンド
│   ├── src/
│   │   ├── components/   # 共通コンポーネント
│   │   ├── views/        # ページコンポーネント
│   │   ├── router/       # Vue Router設定
│   │   ├── assets/       # 静的ファイル
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   └── vite.config.js
├── backend/           # FastAPI バックエンド
│   ├── routers/       # APIルーター
│   ├── main.py        # エントリポイント
│   ├── models.py      # SQLAlchemyモデル
│   ├── schemas.py     # Pydanticスキーマ
│   ├── database.py    # DB接続設定
│   ├── seed.py        # 初期データ投入
│   └── requirements.txt
├── DESIGN.md
├── REQUIREMENTS.md
└── README.md
```

---

## 7. データモデル

### articles
| カラム | 型 | 説明 |
|--------|----|------|
| id | INTEGER PK | 記事ID |
| title | TEXT | タイトル |
| slug | TEXT UNIQUE | URLスラッグ |
| summary | TEXT | 概要文 |
| content | TEXT | 本文（Markdown） |
| category_id | INTEGER FK | カテゴリ |
| author_id | INTEGER FK | 著者（メンバー） |
| published_at | DATETIME | 公開日時 |
| created_at | DATETIME | 作成日時 |

### members
| カラム | 型 | 説明 |
|--------|----|------|
| id | INTEGER PK | メンバーID |
| name | TEXT | 氏名 |
| role | TEXT | 役割（教員/M2/M1/B4等） |
| bio | TEXT | 自己紹介 |
| research | TEXT | 研究テーマ |

### categories
| カラム | 型 | 説明 |
|--------|----|------|
| id | INTEGER PK | カテゴリID |
| name | TEXT | カテゴリ名 |
| slug | TEXT UNIQUE | スラッグ |
