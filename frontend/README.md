# Frontend Docker Setup

バックエンド API と連携する Streamlit フロントエンドアプリケーション

## 機能

- **ホームページ**: バックエンドとの接続確認
- **テキスト変換**: 入力テキストに「by kei」を追加
- **ヘルスチェック**: バックエンドサーバーの状態確認とリアルタイム監視

## セットアップ方法

### 1. Docker を使用した起動

```bash
# フロントエンドのDockerイメージをビルド
docker build -t frontend:latest .

# フロントエンドコンテナを起動（バックエンドが既に起動している前提）
docker run -p 8501:8501 \
  -e BACKEND_URL=http://host.docker.internal:8000 \
  frontend:latest
```

### 2. Docker Compose を使用した起動

```bash
# バックエンドが既に起動していることを確認してから
docker-compose up --build
```

### 3. ローカル開発環境での起動

```bash
# 依存関係をインストール
pip install -r requirements.txt

# アプリケーションを起動
streamlit run app.py
```

## アクセス方法

- フロントエンド: http://localhost:8501
- バックエンド: http://localhost:8000

## 環境変数

- `BACKEND_URL`: バックエンド API の URL（デフォルト: http://localhost:8000）

## API エンドポイント

フロントエンドは以下のバックエンド API エンドポイントを使用します：

- `GET /`: ルートエンドポイント
- `POST /add-signature`: テキストに署名を追加
- `GET /health`: ヘルスチェック

## ファイル構成

```
frontend/
├── app.py              # メインのStreamlitアプリケーション
├── requirements.txt    # Python依存関係
├── Dockerfile         # Dockerイメージ設定
├── docker-compose.yml # Docker Compose設定
└── README.md         # このファイル
```

## 使用技術

- **Streamlit**: Web アプリケーションフレームワーク
- **Requests**: HTTP API クライアント
- **Docker**: コンテナ化
