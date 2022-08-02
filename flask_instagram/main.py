# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import glob
import os

import src.DTO_funcs as dto_funcs
import flask_app as flask_instagram


def main():
    current_path = os.getcwd()
    os.chdir('..')
    back_path = os.getcwd()
    os.chdir('flask_instagram')
    # firebase用のjsonを指定
    cred = credentials.Certificate(
        os.path.join(back_path, 'tokens', 'yamu-myport-firebase.json'))
    other_app = firebase_admin.initialize_app(cred, name='comvi')
    dto_funcs.DB = firestore.client(other_app)
    dto_funcs.CURRENT_PATH = current_path

    flask_instagram.startApp()


if __name__ == "__main__":

    main()
