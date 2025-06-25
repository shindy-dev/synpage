#!/bin/bash
set -e  # エラーがあれば即終了

# マーカーパス
MARKER_FILE="/var/.entrypoint_initialized"

# 初回起動チェック
if [ ! -f "$MARKER_FILE" ]; then
    # 初回起動時処理
    
    # git pull モード指定
    git config --global pull.rebase true
    git config --global user.name "$GITHUB_USER"
    git config --global user.email "$GITHUB_EMAIL"

    # git pull
    (cd /home/dev/github/synpage && git init && git remote add origin https://github.com/shindy-dev/synpage.git && git fetch origin main && git checkout -b main origin/main)

    # マーカーを作成
    touch "$MARKER_FILE"
fi

# /var/custom 内のすべての .sh ファイルを実行
if [ -d /var/custom ]; then
  for script in /var/custom/*.sh; do
    if [ -f "$script" ]; then
      chmod +x "$script"
      bash "$script" || echo "[WARN] $script failed"
    fi
  done
fi

# ディレクトリ移動
cd /home/dev/github/synpage
if [ -f /home/dev/github/synpage/manage.py ] && [ "${DEBUG,,}" != "true" ]; then
    
    # .gitの削除
    rm -rf .git .github .devcontainer docker docs .git* docker* setup.* todo.md requirements.txt
    if command -v git >/dev/null 2>&1; then
        apt update -y && apt purge -y git && apt autoremove -y
        # キャッシュ等削除
        rm -rf /tmp/* /var/tmp/* /root/.cache/*
    fi

    # manage.pyが存在する場合はマイグレーション＆サーバーを実行
    python manage.py makemigrations
    python manage.py migrate
    # 本番環境用に静的ファイル収集
    python manage.py collectstatic --noinput
    exec python manage.py runserver "$@" 
else
    # manage.pyが存在しない場合はbashを実行
    exec /bin/bash
fi