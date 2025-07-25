from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Test Backend by kei", version="1.0.0")

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では具体的なオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    text: str

@app.get("/")
async def root():
    """
    ルートエンドポイント
    """
    return {"message": "Hello World by kei"}

@app.post("/add-signature", response_model=TextResponse)
async def add_signature(request: TextRequest):
    """
    文字列に「by kei」を追加するエンドポイント
    """
    modified_text = f"{request.text} by kei"
    return TextResponse(text=modified_text)

@app.get("/health")
async def health_check():
    """
    ヘルスチェック用エンドポイント
    """
    return {"status": "healthy", "message": "Backend is running by kei"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
