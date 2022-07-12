
from flask import Flask

app = Flask(__name__)
app.config.from_object('flaskApp.config')  # 追加
import flaskApp.main