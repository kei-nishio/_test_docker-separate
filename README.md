# プロジェクト概要

このプロジェクトは、`backend`と`frontend`の 2 つのサービスで構成されています。それぞれが独立した Docker コンテナとして動作し、`frontend`から`backend`の API を呼び出すことができます。

## ディレクトリ構成

```
backend/   # バックエンドサービス (FastAPI)
frontend/  # フロントエンドサービス (Streamlit)
```

## 起動方法

### 1. すべてのサービスを起動

プロジェクト直下にある`start_all.sh`スクリプトを使用して、`backend`と`frontend`を同時に起動できます。

```bash
chmod +x start_all.sh
./start_all.sh
```

### 2. 個別に起動

#### backend

```bash
cd backend
docker-compose up -d
```

#### frontend

```bash
cd frontend
docker-compose up -d
```

## 停止方法

### 1. すべてのサービスを停止

プロジェクト直下にある`stop_all.sh`スクリプトを使用して、`backend`と`frontend`を同時に停止できます。

```bash
chmod +x stop_all.sh
./stop_all.sh
```

### 2. 個別に停止

#### backend

```bash
cd backend
docker-compose down
```

#### frontend

```bash
cd frontend
docker-compose down
```

## 確認方法

### backend

- API のルートエンドポイント: [http://localhost:8000/](http://localhost:8000/)
- ヘルスチェック: [http://localhost:8000/health](http://localhost:8000/health)

### frontend

- アプリケーション: [http://localhost:8501/](http://localhost:8501/)

## 注意事項

- `frontend`の`docker-compose.yml`で`BACKEND_URL`が正しく設定されていることを確認してください。
- 本番環境では、`backend`の CORS 設定で具体的なオリジンを指定してください。
