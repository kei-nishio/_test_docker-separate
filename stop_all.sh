#!/bin/bash

# backendの停止
echo "Stopping backend..."
cd backend
if docker-compose down; then
  echo "Backend stopped successfully."
else
  echo "Failed to stop backend." >&2
  exit 1
fi

# frontendの停止
echo "Stopping frontend..."
cd ../frontend
if docker-compose down; then
  echo "Frontend stopped successfully."
else
  echo "Failed to stop frontend." >&2
  exit 1
fi

# 完了メッセージ
echo "Both backend and frontend have been stopped."
