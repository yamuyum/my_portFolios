

from flask import Flask
from datetime import timedelta  # 時間情報を用いるため

app = Flask(__name__)
app.config.from_object('flaskであそぼ.flaskApp.config')  # 追加

# session設定
app.secret_key = 'session'
app.permanent_session_lifetime = timedelta(hours=1)  # 1時間保持する
