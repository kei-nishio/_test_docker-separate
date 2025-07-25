# FastAPI Backend by kei

このプロジェクトは、DevContainer を使用した FastAPI のテスト用バックエンドです。

## 機能

- 文字列に「by kei」を追加する API
- ヘルスチェック機能
- DevContainer 環境での開発

## エンドポイント

### GET /

ルートエンドポイント。基本的な動作確認用。

### POST /add-signature

文字列に「by kei」を追加します。

**リクエスト:**

```json
{
  "text": "Hello World"
}
```

**レスポンス:**

```json
{
  "text": "Hello World by kei"
}
```

### GET /health

ヘルスチェック用エンドポイント。

## 開発環境のセットアップ

1. VS Code で DevContainer を起動
2. コンテナが自動的に構築され、依存関係がインストールされます
3. ポート 8000 が自動的に転送されます

## サーバーの起動

```bash
python main.py
```

または

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API ドキュメント

サーバー起動後、以下の URL で API ドキュメントにアクセスできます：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
