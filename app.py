# FlaskというWebフレームワークをインポートします
from flask import Flask
import os

# Flaskアプリケーションのインスタンスを作成します
app = Flask(__name__)

# ルートURL ('/') にアクセスがあった場合に、以下の関数を実行します
@app.route('/')
def hello_world():
    # ユーザーに表示するメッセージ
    # 2025年6月15日、北本市よりこんにちは！
    message = "こんにちは、Render！👋 <br>2025年6月15日、埼玉県北本市からデプロイしました。"
    return message

# このファイルが直接実行された場合に、テスト用のサーバーを起動します
# Render環境ではGunicornが使われるため、この部分はローカルテスト用です
if __name__ == "__main__":
    # Renderが利用するPORT環境変数を取得、なければ5000番ポートを利用
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
