## Part 2: インストール手順／環境構築

Django 5.2.3 のインストール手順は、Python 環境の用意から開始し、仮想環境の作成、そして `pip` を用いた Django 本体のインストールまでをカバーする。主要な手順は以下のとおりである。

### 1. Python のインストール
Django は Python 3.8 以降を要件としている。本ドキュメントでは Python 3.13 を前提とする。  
- **Ubuntu**: `sudo apt update && sudo apt install python3 python3-venv python3-pip`  
- **macOS**: Homebrew から `brew install python`  
- **Windows**: 公式サイトから [Python 3.13](https://www.python.org/downloads/windows/) をダウンロードしてインストール  

### 2. 仮想環境の作成
プロジェクトごとに依存関係を分離するため、仮想環境を使用する。  
```bash
python3 -m venv venv     # Python 標準の仮想環境を作成
source venv/bin/activate # Linux/macOS の場合
venv\Scripts\activate  # Windows の場合
```  
仮想環境作成後、ターミナルに `(venv)` と表示されれば成功。

### 3. pip のアップグレード
`pip` のバージョンが古い場合、以下のコマンドで最新化する。  
```bash
pip install --upgrade pip
```  
最新版確認は `pip --version` で実行可能。

### 4. Django のインストール
仮想環境内で `pip` を用いて Django 5.2.3 をインストールする。  
```bash
pip install Django==5.2.3
```  
公式リリースノートにも記載のとおり、LTS 版である 5.2.3 を指定することが推奨される。インストール完了後、`python -m django --version` でバージョンを確認できる。

### 5. プロジェクトの初期化
Django プロジェクトを新規作成するために、`django-admin` コマンドを実行する。  
```bash
django-admin startproject mysite
```  
このコマンドにより、`mysite/` 以下に以下のような基本構成が生成される。  

```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

### 6. 開発サーバーの起動
プロジェクトディレクトリに移動し、開発用サーバーを起動する。  
```bash
cd mysite
python manage.py runserver
```  
デフォルトでは `http://127.0.0.1:8000/` でアクセス可能となる。

### 7. データベース設定（SQLite）
デフォルトでは SQLite が使用される。`settings.py` の `DATABASES` セクションを編集して、他のデータベース（PostgreSQL、MySQL など）に切り替え可能である。

### 参考文献
- [Django 公式ドキュメント: Installation](https://docs.djangoproject.com/en/5.2/topics/install/)  
- [Django 公式ダウンロードページ](https://www.djangoproject.com/download/)  
- [Python.org: Download Python](https://www.python.org/downloads/)  
- DigitalOcean: [How To Install the Django Web Framework on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04)  
- Django PyPI: [Django 5.2.3 on PyPI](https://pypi.org/project/Django/)

Next ... [Part 3: ファイル構成の詳細](part3.md)