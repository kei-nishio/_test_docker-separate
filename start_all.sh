#!/bin/bash

# backendの起動
echo "Starting backend..."
cd backend
if docker-compose up -d; then
  echo "Backend started successfully."
else
  echo "Failed to start backend." >&2
  exit 1
fi

# frontendの起動
echo "Starting frontend..."
cd ../frontend
if docker-compose up -d; then
  echo "Frontend started successfully."
else
  echo "Failed to start frontend." >&2
  exit 1
fi

# 完了メッセージ
echo "Both backend and frontend are up and running."
