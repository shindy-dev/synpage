FROM python:3.13.3-slim

ARG WORKSPACE=/home/dev/github/synpage

# 対話式コンソールの処理をスキップ
ENV DEBIAN_FRONTEND=noninteractive

# 使用するポートの宣言（Web/Django）
EXPOSE 8000

# パッケージのインストール
RUN apt update -y && apt upgrade -y && apt install -y git && apt autoremove -y && apt autoclean -y

# コンテナ起動時の作業ディレクトリ
WORKDIR ${WORKSPACE}

# pipでインストールするパッケージリストのコピー
COPY docker/requirements.txt ${WORKSPACE}/requirements.txt

# venv環境の作成＆パッケージインストール
RUN python -m venv ${WORKSPACE}/.venv && ${WORKSPACE}/.venv/bin/pip install --no-cache-dir -r ${WORKSPACE}/requirements.txt

# venv環境のpythonをデフォルトとして設定
ENV PATH="${WORKSPACE}/.venv/bin:$PATH"

# キャッシュ等削除
RUN rm -rf /tmp/* /var/tmp/* /root/.cache/* ${WORKSPACE}/requirements.txt

# サーバ初期化後に処理したいスクリプト(entrypoint.sh内でコール)をコピー
COPY docker/scripts/postprocessing.sh /var/custom/postprocessing.sh
RUN chmod +x /var/custom/postprocessing.sh

# エントリーポイント（コンテナ起動時の動作）設定
COPY docker/scripts/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# docker run 時のデフォルトコマンド
# docker run <image> <ip>:<port>で任意のip:portを指定可能
CMD ["0.0.0.0:8000"]