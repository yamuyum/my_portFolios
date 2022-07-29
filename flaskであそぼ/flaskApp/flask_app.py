# coding: utf-8
from flaskであそぼ.flaskApp import app
from .src import testFunc
from flask import render_template, redirect, url_for, request, session


@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['title1', 'title2', 'title3']
    }
    # htmlでの名前=ここ(python上の名前)
    return render_template('index.html', my_dict=my_dict)


@app.route('/test')
def test_1():
    return render_template('test1.html')


@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータ受け取ったので処理します')
    req1 = request.form['data1']

    value = testFunc.testFunction(req1)

    return f'POST受け取ったよ: {value}'


def startApp():
    app.run(debug=True)
