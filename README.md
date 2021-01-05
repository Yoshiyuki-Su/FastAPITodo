# FastAPITodo
FastAPIを利用したTodoアプリケーション

# Installation
## jinja2のインストール
```bash
pip install jinja2
```
## FastAPIのインストール
```bash
pip install fastapi uvicorn
```
## SQLAlchemyのインストール
```bash
pip install sqlalchemy
```
## python-multipartモジュールをインストール
フォームデータを使用するためにインストール
```bash
pip install python-multipart
```

# サーバーの立ち上げ
```bash
python run.py
```

# データベースの作成とサンプルデータの挿入
```bash
python create_table.py
```

# データの確認
```bash
$ sqlite3 db.sqlite3

sqlite> .table
sqlite> select * from user;
sqlite> select * from task;
```

# WebAPIとしてコンソールからデータを取得する
## ログインユーザのタスクを取得する
```bash
curl -u username:password http://127.0.0.1:8000/get
```

# 参考  
> https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment
  
