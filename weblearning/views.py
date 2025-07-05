import random
import time
import os

from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import render
import markdown

docs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "markdown", "documents")
docs_list = [ os.path.splitext(f)[0] for f in  os.listdir(docs_path) if os.path.isfile(os.path.join(docs_path, f))]

def _markdown_page(request, dirpath, filename, title):
    # アプリのディレクトリを取得
    app_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(app_dir, dirpath, filename)

    if not os.path.exists(md_path):
        return render(request, '404.html', status=404)

    with open(md_path, encoding='utf-8') as f:
        md_content = f.read()

    md = markdown.Markdown(extensions=["toc", "attr_list", "md_in_html", 'fenced_code', 'tables'])
    html = md.convert(md_content)
    return render(request, 'weblearning/markdown_page.html', {'content': html, 'title': title, 'toc_html': md.toc, 'docs_list': docs_list})

@login_required
def index(request):
    return _markdown_page(request, 
                          dirpath="markdown", 
                          filename="HOME.md", 
                          title="HOME")
    

@login_required
def playground(request):
    return render(request, "weblearning/pages/playground.html",  {'title': "Playground", 'docs_list': docs_list})

@login_required
def count(request):
    return render(request, "weblearning/pages/count.html",  {'title': "Count", 'docs_list': docs_list})

@login_required
def table(request):
    return render(request, "weblearning/pages/table.html",  {'title': "Table", 'docs_list': docs_list})

@login_required
def table_api_data(request):
    time.sleep(2)
    response = {
        "items": [
            {
                "ID": i,
                "Name": f"Item {random.randint(1, 1000)}",
                "Value": random.randint(1, 1000),
            }
            for i in range(1, 101)
        ]
    }

    return JsonResponse(response)

@login_required
def docs(request, doc_type: str):
    if doc_type not in docs_list:
        raise Http404("Document type not found.")
    return _markdown_page(request, 
                          dirpath=os.path.join("markdown", "documents"), 
                          filename=f"{doc_type}.md",
                          title=f"{doc_type.upper()} Documents")
    