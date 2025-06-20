FROM python:3.13.3-slim

# 対話式コンソールの処理をスキップ
ENV DEBIAN_FRONTEND=noninteractive

# 使用するポートの宣言（Web/Django）
EXPOSE 8000

# 必要パッケージのインストール
RUN apt update && apt upgrade -y && \
    apt install -y git curl bzip2 && \
    apt autoremove -y && apt autoclean -y

# Micromamba のインストール
RUN curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C /usr/local/bin --strip-components=1 bin/micromamba

# pipでインストールするパッケージリストのコピー
COPY docker/requirements.txt /root/requirements.txt

# micromamba で仮想環境作成（synpage用）
RUN micromamba create -y -n synpage python=3.13 && \
    micromamba run -n synpage python -m pip install --no-cache-dir -r /root/requirements.txt && \
    micromamba clean --all --yes && \
    micromamba shell init -s bash && \
    sed -i '$a micromamba activate synpage' /root/.bashrc

# キャッシュ等削除
RUN rm -rf /tmp/* /var/tmp/* /root/.cache/*

# コンテナ起動時の作業ディレクトリ
WORKDIR /home/dev/github/synpage

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