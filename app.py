# FlaskというWebフレームワークをインポートします
from flask import Flask
import os
# ★ datetimeモジュールをインポート
from datetime import datetime
import pytz # タイムゾーンを扱うためにインポート

# Flaskアプリケーションのインスタンスを作成します
app = Flask(__name__)

# ルートURL ('/') にアクセスがあった場合に、以下の関数を実行します
@app.route('/')
def hello_world():
    # ★ 日本のタイムゾーンを取得
    jst = pytz.timezone('Asia/Tokyo')
    # ★ 現在の日時を日本のタイムゾーンで取得
    now = datetime.now(jst)
    # ★ f-stringを使って、フォーマットした日時をメッセージに埋め込む
    now_str = now.strftime('%Y年%m月%d日 %H時%M分%S秒')

    # ユーザーに表示するメッセージ
    message = f"""
    こんにちは、Render！👋 <br>
    ただいまの時刻は <strong>{now_str}</strong> です。<br>
    埼玉県北本市からデプロイしました。
    """
    return message

# このファイルが直接実行された場合に、テスト用のサーバーを起動します
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
