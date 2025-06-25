
# Part 5: 実際のコーディングフローとサンプルコード（Django 5.2.3）

本章では、Django を用いた Web アプリケーション開発の典型的なフローと、それに伴うサンプルコードについて解説します。対象バージョンは Django 5.2.3 です。

---

## 1. プロジェクトの作成

まずは Django プロジェクトの作成から始めます。

```bash
django-admin startproject myproject
cd myproject
```

このコマンドにより、以下のようなディレクトリ構成が作成されます。

```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 2. アプリケーションの作成

Djangoでは、機能ごとに「アプリケーション（app）」を作成して構築していきます。

```bash
python manage.py startapp blog
```

```
myproject/
├── blog/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

`blog` をアプリケーション名としています。

---

## 3. モデルの定義（models.py）

データベースと連携するクラスを定義します。

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## 4. モデルのマイグレーション

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. 管理画面への登録（admin.py）

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

---

## 6. ビューの作成（views.py）

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

---

## 7. テンプレートの作成

`blog/templates/blog/post_list.html` を作成します。

```html
<!DOCTYPE html>
<html>
<head>
    <title>ブログ一覧</title>
</head>
<body>
    <h1>投稿一覧</h1>
    {% for post in posts %}
        <div>
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
        </div>
    {% endfor %}
</body>
</html>
```

---

## 8. URL の設定

`blog/urls.py` を作成します。

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

`myproject/urls.py` にアプリケーションの URL を組み込みます。

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

## 9. 開発サーバーの起動

```bash
python manage.py runserver
```

`http://127.0.0.1:8000` にアクセスすると、一覧ページが表示されます。

---

# 参考文献

- [Django 公式ドキュメント](https://docs.djangoproject.com/ja/5.2/)
- [Django チュートリアル（公式）](https://docs.djangoproject.com/ja/5.2/intro/)
- [Django GitHub リポジトリ](https://github.com/django/django)

