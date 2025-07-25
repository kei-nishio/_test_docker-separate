#!/bin/bash

# フロントエンド起動スクリプト

echo "🚀 フロントエンドアプリケーションを起動しています..."

# バックエンドの接続確認
echo "📡 バックエンドサーバーとの接続を確認中..."
if curl -f http://host.docker.internal:8000/health > /dev/null 2>&1; then
    echo "✅ バックエンドサーバーが利用可能です"
else
    echo "⚠️  バックエンドサーバーに接続できません。バックエンドが起動していることを確認してください。"
fi

# Dockerイメージをビルド
echo "🔨 Dockerイメージをビルド中..."
docker build -t frontend:latest .

# コンテナを起動
echo "🐳 Dockerコンテナを起動中..."
docker run -p 8501:8501 \
  -e BACKEND_URL=http://host.docker.internal:8000 \
  frontend:latest

echo "🎉 フロントエンドアプリケーションが起動しました!"
echo "📱 アクセスURL: http://localhost:8501"
