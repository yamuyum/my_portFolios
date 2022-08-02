# coding: utf-8
from flask import render_template, redirect, url_for, request, session
from flask import Flask
from datetime import timedelta  # 時間情報を用いるため
import src.DTO_funcs as dto_func

app = Flask(__name__)
# ここ本来はバレないような文字列で
app.secret_key = 'session'
app.permanent_session_lifetime = timedelta(
    hours=1)  # (minutes=5)-> 5分 #(days=5) -> 5日保存
# from master_tools import app


@app.route('/')
def index():
    '''
    初期画面
    '''
    session.permanent = True  # セッション初期化
    post_data_list = dto_func.get_dbdatas(
        "flask_instagram/flask_instagram/posts")

    # 本当はここクラス定義して色々関数やフィールド定義した方がやりやすいが、
    # 投稿だけ表示なら、作るのめんどくさいからベタでおく。。。

    current_user = {
        "uid": "aaa",
        "name": "name",
        "ingUrl": "",
        "is_authenticated": True
    }
    # htmlでの名前=ここ(python上の名前)
    return render_template('index.html', postDatas=post_data_list, currentUser=current_user)


def startApp():
    app.run(debug=True)


# # おまじない
# if __name__ == "__main__":
#     app.run(debug=True)
