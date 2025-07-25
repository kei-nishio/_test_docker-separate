import streamlit as st
import requests
import json
import os

# バックエンドのURL設定
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def call_backend_api(endpoint, method="GET", data=None):
    """バックエンドAPIを呼び出す関数"""
    try:
        url = f"{BACKEND_URL}{endpoint}"
        
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"APIエラー: {e}")
        return None

def main():
    """メイン関数"""
    st.title("🚀 Frontend App by kei")
    st.markdown("バックエンドAPIと連携するStreamlitアプリケーション")
    
    # サイドバーでページ選択
    page = st.sidebar.selectbox(
        "ページを選択:",
        ["ホーム", "テキスト変換", "ヘルスチェック"]
    )
    
    if page == "ホーム":
        show_home_page()
    elif page == "テキスト変換":
        show_text_conversion_page()
    elif page == "ヘルスチェック":
        show_health_check_page()

def show_home_page():
    """ホームページ"""
    st.header("🏠 ホームページ")
    
    st.markdown("""
    ### このアプリについて
    このアプリケーションは以下の機能を提供します：
    
    - **テキスト変換**: 入力したテキストに「by kei」を追加
    - **ヘルスチェック**: バックエンドサーバーの状態確認
    
    左側のサイドバーからページを選択してください。
    """)
    
    # バックエンドのルートエンドポイントを呼び出し
    with st.spinner("バックエンドと接続中..."):
        result = call_backend_api("/")
        if result:
            st.success("✅ バックエンドとの接続が確認できました")
            st.json(result)
        else:
            st.error("❌ バックエンドに接続できませんでした")

def show_text_conversion_page():
    """テキスト変換ページ"""
    st.header("✏️ テキスト変換")
    
    st.markdown("入力したテキストに「by kei」を追加します。")
    
    # テキスト入力
    input_text = st.text_area(
        "変換したいテキストを入力してください:",
        placeholder="ここにテキストを入力...",
        height=100
    )
    
    # 変換ボタン
    if st.button("🔄 変換実行", type="primary"):
        if input_text.strip():
            with st.spinner("変換中..."):
                data = {"text": input_text}
                result = call_backend_api("/add-signature", method="POST", data=data)
                
                if result:
                    st.success("✅ 変換完了!")
                    st.markdown("### 変換結果:")
                    st.text_area(
                        "変換後のテキスト:",
                        value=result["text"],
                        height=100,
                        disabled=True
                    )
                    
                    # コピーボタン（JavaScript使用）
                    st.markdown(f"""
                    <script>
                    function copyToClipboard() {{
                        navigator.clipboard.writeText(`{result["text"]}`);
                    }}
                    </script>
                    <button onclick="copyToClipboard()">📋 コピー</button>
                    """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ テキストを入力してください。")

def show_health_check_page():
    """ヘルスチェックページ"""
    st.header("🏥 ヘルスチェック")
    
    st.markdown("バックエンドサーバーの状態を確認します。")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 ヘルスチェック実行", type="primary"):
            with st.spinner("チェック中..."):
                result = call_backend_api("/health")
                
                if result:
                    st.success("✅ バックエンドは正常に動作しています")
                    st.json(result)
                else:
                    st.error("❌ バックエンドに問題があります")
    
    with col2:
        if st.button("🔄 ルートエンドポイント確認"):
            with st.spinner("確認中..."):
                result = call_backend_api("/")
                
                if result:
                    st.success("✅ ルートエンドポイントは正常です")
                    st.json(result)
                else:
                    st.error("❌ ルートエンドポイントに問題があります")
    
    # サーバー情報表示
    st.markdown("---")
    st.markdown("### 🖥️ サーバー情報")
    st.markdown(f"**バックエンドURL:** `{BACKEND_URL}`")
    
    # リアルタイム監視（オプション）
    if st.checkbox("🔄 リアルタイム監視（10秒間隔）"):
        placeholder = st.empty()
        
        import time
        for i in range(6):  # 1分間監視
            with placeholder.container():
                result = call_backend_api("/health")
                if result:
                    st.success(f"✅ 監視中 - 正常動作 ({i+1}/6)")
                    st.json(result)
                else:
                    st.error(f"❌ 監視中 - 問題検出 ({i+1}/6)")
                
            if i < 5:  # 最後の反復では待機しない
                time.sleep(10)

if __name__ == "__main__":
    # ページ設定
    st.set_page_config(
        page_title="Frontend App by kei",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # カスタムCSS
    st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    main()
