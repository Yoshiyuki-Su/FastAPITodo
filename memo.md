# サーバーの立ち上げ
python run.py

# jinja2のインストール
pip install jinja2

# FastAPIのインストール
pip install fastapi uvicorn

# SQLAlchemyのインストール
pip install sqlalchemy

# フォームデータを使用するには、python-multipartモジュールをインストール
pip install python-multipart

# データベースの作成とサンプルデータの挿入
python create_table.py

# データの確認
$ sqlite3 db.sqlite3

sqlite> .table
sqlite> select * from user;
sqlite> select * from task;

# WebAPIとしてコンソールからデータを取得する
## ログインユーザのタスクを取得する
curl -u username:password http://127.0.0.1:8000/get

# 参考
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment
