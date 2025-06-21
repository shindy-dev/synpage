## Part 4: コーディングフロー（モデル・ビュー・テンプレート）

DjangoのWeb開発は、Model、View、Template（MVT）の三つの役割を分離して実装することで、コードの可読性と保守性を高める設計思想に基づいている。以下では、基本的なコーディングフローを示す。

### モデル（Model）の作成
モデルはデータベースと対応するPythonクラスとして定義され、テーブル構造やフィールドの型・制約を記述する。例えば、書籍情報を管理する `Book` モデルは次のように定義する:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
```

モデル定義後、マイグレーションファイルを生成し、データベースを変更する:

```bash
python manage.py makemigrations  # モデルの変更を検知してマイグレーションファイルを作成
python manage.py migrate       # マイグレーションを適用し、テーブルを作成
```

### ビュー（View）の実装
ビューはHTTPリクエストを処理し、レスポンスを返すビジネスロジックを記述する箇所である。関数ベースビュー（FBV）の例を示す:

```python
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
```

クラスベースビュー（CBV）を用いる場合は、以下のように記述できる:

```python
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
```

### テンプレート（Template）の作成
テンプレートはHTMLとDjangoテンプレート言語を組み合わせてUIを記述する。`books/book_list.html` の例:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>書籍一覧</title>
</head>
<body>
    <h1>書籍一覧</h1>
    <ul>
    {% for book in books %}
        <li><a href="{% url 'book_detail' book.pk %}">{{ book.title }}</a> - {{ book.author }}</li>
    {% empty %}
        <li>書籍が登録されていません。</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### 実際の開発フロー例
1. アプリケーション作成:
   ```bash
   python manage.py startapp books  # 新規アプリ 'books' を作成
   ```
2. `books` を `settings.py` の `INSTALLED_APPS` に追加
3. モデルを定義し、マイグレーション実行
4. ビューとURLパターンを設定:
   ```python
   # mysite/urls.py
   from django.urls import path, include

   urlpatterns = [
       path('books/', include('books.urls')),
   ]
   ```
   ```python
   # books/urls.py
   from django.urls import path
   from .views import book_list, book_detail

   urlpatterns = [
       path('', book_list, name='book_list'),
       path('<int:pk>/', book_detail, name='book_detail'),
   ]
   ```
5. テンプレート作成およびスタイル調整
6. 開発サーバー起動で動作確認:
   ```bash
   python manage.py runserver  # http://127.0.0.1:8000/books/ で一覧表示
   ```

以上が、基本的なMVTに基づくコーディングフローである。

Next ... [Part 5: 実際のコーディングフローとサンプルコード（Django 5.2.3）](part5.md)