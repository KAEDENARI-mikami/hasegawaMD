# 長谷川ゼミ 公式サイト

## 起動方法

### バックエンド（FastAPI）
```bash
cd backend
pip install -r requirements.txt
python seed.py       # 初回のみ（DBとカテゴリを初期化）
uvicorn main:app --reload
```
→ http://localhost:8000
→ APIドキュメント: http://localhost:8000/docs

### フロントエンド（Vue.js）
```bash
cd frontend
npm install
npm run dev
```
→ http://localhost:5173

## ページ構成

| ページ | パス | 説明 |
|--------|------|------|
| ホーム | `/` | ゼミ概要・最新成果・ニュース |
| ゼミ紹介 | `/about` | 理念・研究分野・活動内容 |
| 成果発表 | `/results` | 研究成果一覧 |
| メンバー | `/members` | 教員・学生メンバー |
| ニュース | `/news` | お知らせ一覧 |

## コンテンツの追加方法

バックエンドが起動した状態で http://localhost:8000/docs を開くとAPIドキュメントが確認できます。  
記事・メンバー情報はDBに直接追記するか、後から管理画面を実装して追加してください。
