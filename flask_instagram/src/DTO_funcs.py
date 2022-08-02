# coding: utf-8
import math
import datetime
import os
import glob
from typing import Any
import openpyxl
import random


CURRENT_PATH = ""
DB = "11"

DT_NOW = datetime.datetime.now().strftime('%y%m%d')
DT_YEAR = datetime.datetime.now().strftime('%Y')
DT_MONTH = datetime.datetime.now().strftime('%m')

# ーーーーーーーーーーーーDBデータ取得系ーーーーーーーーーーーーー


def get_dbdatas(coll_path: Any):
    '''
    cパスから以下全てのデータを取得する
    '''
    output_db_datas = []

    docs_datas = DB.collection(coll_path).stream()
    for doc_data in docs_datas:
        # print(f"{doc_data.id}")
        data = doc_data.to_dict()
        output_db_datas.append(data)

    return output_db_datas

# ーーーーーーーーーーーーDBデータ操作系ーーーーーーーーーーーーー


def main():
    # テストで動かす時

    print(0)


if __name__ == "__main__":
    main()
